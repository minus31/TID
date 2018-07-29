# BATCH NORMALIZATION  

--------

#### * Flow 

1. 딥러닝의 고질적인 문제 
2. Batch Normalization 이란 
3. How to Use ( training / Inference )
4. 자체적인 실험 
5. 누군가 있다면 질문하고 싶은 부분

-------

 가장 먼저 Batch Normalization하는 수식을 보겠습니다.  

$\star \  Input = \{x_1, x_2  \cdots x_m\} , m = batch size $

$\star \  output = \hat{x} = \dfrac{(x_i-  \mu_{\beta})}{\sqrt{\sigma^2_{\beta} + \epsilon}} => \gamma \hat{x} + \beta , \\ \star \ \gamma, \beta => parameters$

#### 1. 딥러닝의 고질적인 문제 

 딥러닝을 공부하게 되면, 뭐만 하면 Gradient 가 사라지고, 뭐만 하면 Overfitting 된다고 합니다. 그 이유도 너무 다양해서 공부 할 때 마다, 머릿 속으로 다시 떠올려 보게 되는데요. 역시 가장 큰 문제는 역시 layer가 깊어지기 때문에 생기는 겁니다. 망이 깊어지게 되면 거의 모든 문제를 풀 수 있겠지만, 시간이나 computational resource 가 많이 들고, 위에 말한 Gradient vanishing/exploding, Overfitting으로 인한 일반성(Generalization)의 감소 등이 발생하게 됩니다. 깊은 망에서도 Gredient가 잘 흘러가고(activation func - ReLu, 좋은(?)loss function, careful initialization), Overfitting이 되지 않도록 하는 방법(Dropout, kernel regularizer, photometric distortion(or data augmentatio) 등등!)들과 깊은 망을 쌓아도 학습을 잘 할 수 있는 아키텍쳐들이 많이 만들어졌습니다. 

 논문에서는 문제점의 원인을 데이터 자체에서 찾았습니다. 이러한 방법 들을 사용하더라도, The distribution of nonlinearity Input 에 대한 문제는 해결되지 않아서 근본적인 방안이 아니라고 합니다. 문제를 정확히 정의 하면, Changing the distribution of nonlinearity input, 이른바 ***Internal Covariate Shift*** 입니다. Internal Covariate Shift 는 Network 안에서 입력의 분포가 달라지는 것을 말합니다. Neural Network 에서 이전 레이어의 아웃풋이 다음 레이어의 인풋이 되는데요. 이 때, 이전 레이어의 아웃풋은,  weight 와 bias가 곱해지고 더해져서 만들어진 겁니다. 물론 거기에 활성화 함수까지 통과를 합니다. 게다가 미니배치 단위로 가중치를 업데이트 하기 때문에 weight는 미니배치가 어떻게 구성되었는지에 영향을 받게 됩니다. 이러한 이유들로 이전 레이어의 parameter(의 변화)로 인해 다음 레이어 인풋의 분포가 달라질 수 있는데, 이 현상을 Internal Covariate Shift 라고 합니다. 언급한 것 처럼 Internal Covariate Shift의 원인을 Parameter 몇 몇이 너무 커지는 것 때문이라고 합니다(파라미터 평균 값보다 큰 파라미터라고도 표현 합니다.). 생각 해보면 Shallow model을 모델을 만들 때도, 특정 데이터에 대한 Parameter가 건전하지 않은 이유로 커지는 상황이 있는데요. 그 건전하지 않은 이유 중 가장 대표적인 것이 각 변수간의 Scale의 차이였습니다. 논문에서도 Neural Network 에서 인풋이 whitened, Linearly transfromed to zero mean, unit variance, decorrelated가 되었을 때, Converge를 빨리 한다고 주장합니다. 이에 대해서 좋은 설명을  [JunsikWhang님 블로그](https://jsideas.net/python/2018/01/28/batch_normalization.html) 에서 해주셔서 빌려옵니다. 두 가지의 loss function이 있을 때, 어느 쪽이 더 빨리 수렴하는 지 한눈에 볼 수 있는 실험입니다. 

1. $h_1(x) = \dfrac{x^2}{20} + y^2$
2. $h_2(x) = x^2  + y^2 $

이 두가지 loss가 있을 때,  둘의 차이점은 1.의 경우 x에 붙은 분모 때문에 x가 loss에 미치는 영향이 그만 큼 줄어듭니다. x를 x축, y를 y축으로 하면, 1.loss의 그래프는 2.loss보다 가로로 길쭉해지겠습니다. 그리고 Converge하는 과정을 붉은 선으로 묘사하면 아래와 같겠습니다. 

![](https://www.dropbox.com/s/8d8uif1md9dny2f/Screenshot%202018-07-26%2011.54.12.png?raw=1)

확실히 차이가 나겠지요. 

#### 2. Batch Normalization 이란 

 저는 따라서 Batch Normalization의 목적을 Scale의 차이 때문에 생기는 Parameter의 변화로 다음 레이어의 인풋의 분포가 달라지지 않도록, 평균을 0, 분산을 1로 함으로써 방지하는 것이라고 해석했습니다. 

$\star \  Input = \{x_1, x_2  \cdots x_m\} , m = batch size $

$\star \  output = \hat{x} = \dfrac{(x_i-  \mu_{\beta})}{\sqrt{\sigma^2_{\beta} + \epsilon}} => \gamma \hat{x} + \beta , \\ \star \ \gamma, \beta => parameters$

 그냥 whitening을 할 수도 있는데, 왜 Batch Normalization을 하는 걸까요? 위의 수식으로도 알 수 있듯이, 사실 batch normalization과 whitening은 그리 다른 것이 아닙니다. Batch Normalization의 차이점은 $\gamma , \beta$의 존재 입니다. 이 둘의 역할은 무엇일까요. 그냥 whitening을 할때는 최적화 과정과 무관하게 진행되기 때문에 특정 파라미터가 커진 상태로 계속 whitening이 진행될 가능성이 존재합니다. 이전 레이어의 아웃풋에 대한 whitening이 이전 레이어의 파라미터의 변화에 영향을 받지 않기 때문입니다. 그래서 Batch Normalization은 최적화 과정에서 학습하는 파라미터 두가지를 whitening 한 뒤 곱하고($\gamma$) 더했습니다($\beta$). 이 또한 역시 미니 배치 단위로 학습을 하기 때문에 미니배치 단위로 평균과 분산을 구해서 whitening 해주었습니다. 이 두 파라미터를 추가 함으로써, 학습간에 정규화 하는 정도를 정할 수 있고, $\gamma$ 가 표준편차, $\beta$ 가 평균이라면, 정규화 되기 전으로 돌리는 identity mapping도 가능 해졌기 때문에, 좀 더 강력한 방법이라고 할 수 있습니다. 

######  Batch normalization 의 효과 

1. Regularization 효과 

   (스케일의 차이에 따라 다르게 적용된다. dropout이나 l_1, l_2 weight decay, photometric Distortion을 안 써도 괜찮다고 한다.  )

2. 모델의 최적화를 빠르게 할 수 있다. (또한 안정적)

진짜로 그런지는 밑에서 실험을 통해 알아보겠습니다.

#### 3. How to Use

######  Training  

 Batch Normalization도 하나의 extra layer로, 보통 비선형함수 앞에 위치하게 됩니다. 

![](https://www.dropbox.com/s/yvocycenduq1hxy/Screenshot%202018-07-26%2015.10.37.png?raw=1)

back propagation에서 아래의 chain rule 따라 $\gamma$, $\beta$ 에 의한 loss의 미분값을 구합니다. 이 미분값을 구하는 과정은 아직도 공부 중에 있습니다. 

<img src="https://www.dropbox.com/s/vi22m8d29xbw3xn/Screenshot%202018-07-26%2015.15.50.png?raw=1" width="200" height="100">

> * **CNN 에서의 Batch Normalization**
>
>    Convolutional Neural Network에서의  Batch Normalization은 그의 특성을 살리기 위해서 Batch size를 다르게 합니다.
>
>   예를 들어, Batch size = 24 이고,  feature map 의 사이즈 = (100, 100) 이고 Feature map의 개수 = 32 라고 하겠습니다. 이 경우에는  Batch size(24)  * 100 * 100 개의 숫자로 구한 평균 과 분산으로 Normalize하고 feature map의 개수 만큼, 32개의 $\gamma$ 와 $\beta$ 를 만들어 업데이트 합니다. 

###### Inference 

먼저 논문에 나온  Inference 내용을 캡쳐 해봤습니다. 

<img src="https://www.dropbox.com/s/p6vhrjg3vsxoqk1/Screenshot%202018-07-26%2016.09.12.png?raw=1" width="400" height="">

Test를 할때에는 평균 값은 = mini batch 간의 평균의 평균 값을,  분산값은 mini batch 분산의 평균을 사용 하되, 통계학적으로 Unbiased variance 에는 Bessel's correlation을 통해 보정해야 함으로 $\dfrac{m}{m-1}$ (m이 커지면 1에 가까워진다.)

#### 4. 자체적인 실험  

 따로 다른 데이터 셋에 대해 실험 하기보다, 지금 제가 개발 중인 모델의 BN을 적용하기 전과 적용한 후를 비교해 보았습니다. 결과는 아래와 같습니다. (BN 외에는 다른 조건을 모두 동일 하게 했습니다.)

No BN             |  BN
:-------------------------:|:-------------------------:
![](https://www.dropbox.com/s/ktlioon0swyicd9/Screenshot%202018-07-27%2011.39.01.png?raw=1)  | ![](https://www.dropbox.com/s/30xjzff9femt8vb/Screenshot%202018-07-27%2011.58.52.png?raw=1) 

그런데…. 별 차이가 없고, BN을 적용 했을 때, 오히려 Validation_loss에 대해서는 더 변동이 심했습니다. 하지만 Training loss만 보면 BN을 적용했을 때,  훨씬 빨리 수렴했단 것을 알 수 있습니다. 사실 제가 만들고 있는 모델에 사용하는 데이터가 갯수도 적고, 컨디션도 나빠서 저렇게 나온 것 같습니다. 위 그래프로는 효과가 잘 안 보일 수 있겠지만, 개인적으로  모델을 계속 개발하는데에 있어서, BN을 적용한 뒤 훨씬 안정적인 학습을 하고 있습니다.

####  5. 누군가 있다면 질문하고 싶은 부분

1. Normalization 시에 사용하는 배치의 분산이 '0'이 됬을 때, 문제가 생기는 것을 방지하는 작은 상수 $\epsilon$ 은 구현 시에 정확이 얼마의 값을 넣는가?





















