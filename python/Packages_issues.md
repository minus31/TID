### argparse module

------------

>  ```pip install argparse  ```
>
> ```import arge parse```

* 명령행 인자 ? ([link][http://data-forge.blogspot.com/2012/01/blog-post_3593.html])

 Main 함수를 사용할 때, 보통 리턴값이 없는 void main() 형이나 리턴값 0을 반환하는  int void() 등과 같은 형식을 많이 볼 수 있다.

그러나 main 함수의 원형은 다음과 같은 모습으로 선언되어져 있다.

int main(int argc, char* argv[])

그리고 이 int main(int argc, char* argv[]) 을 사용하면
처음 작성한 프로그램을 실행할때 설정한 값을 넣어서 작성한 프로그램을 돌릴 수 있다.

int argc 는 "argument count"의 줄임말로 해석 되며, 명령행 인자에 넣언 인자 값의 수를 담는 정수형 변수이다.

char *argv[] 는 실제 명령행 인자값이 저장 되는 문자 형식의 포인터 배열이다.

예를 들어,

1000 라인 정도의 데이터를 가지고 있는 text 파일을 읽어 들여 데이터를 처리하는 test.exe 라는 프로그램이 있다고 하자,

실질적으로 100 라인에서 200 라인 사이에 있는  데이터만을 사용해도 문제가 없는 일을 한다고 가정해 보면.

이런때 1000라인을 모두 읽어 들인다면, 엄청난 시간 낭비가 될 것이다.

(물론 요즘 컴퓨터는 저 정도 양의 데이터 처리에 많은 시간을 허비 하지 않는다. 단순히 단적인 예를 위해 제시한 상황이다.)

이때 1000라인을 모두 읽어 들이는 시간 낭비를 하지 않고도

데이터 처리에 실질적으로 필요한 100 라인에서 200 라인 까지만 읽어라 라고 프로그램에게 처음 부터 명령을 줄 수 있게 해주는 것이

바로 이 "명령행 인자" 이다.

* 사용법 ! ([link](http://discreteglissando.com/2014/08/22/argparse-module/))

### .bashrc 와 .bash_profile 의 차이 

* .bash_profile은 login shell이고 .bashrc는 not login shell
* bash_profile은 서버에 로그인 할때 실행이 되고, .bashrc는 새로운 쉘이
  생성될때 실행이 됩니다.



### pyenv 환경 Path (1 / 21, 2018)

**/Users/MAC/.pyenv/versions/anaconda3-4.4.0/envs/python_al**



### Pyenv  설정 시 (2 /4 , 2018) 

pyenv 새로 만들려면, 그 환경에 얹고 싶은 파이썬 버전이나 아나콘다 버전을 pyenv 로 다운 받아야 그 버전으로 virtualenv 만들때 만들어진다. 

pyenv install —list

pyenv install 3.6.1

pyenv virtualenv 3.6.1 {환경 name}

pyenv version

pyenv activate {환경 이름 }

이렇게 하면, 내부 디렉토리 구조는 

그환경 (예로들면 3.6.1)이 만들어지고

그다음 virtualenv 로 환경을 만들면 

{환경이름}으로 그 해당 환경 디렉토리와 연결되어있는(연결되어있겠지? ) 디렉토리 생성됨





### Jupyter extensions (2 /4 , 2018)

enable 하는데 까지 힘들었다. 

사실 conda로 forge 해서 다운로드 하면 enable도 자동으로 해주었다. 이때 바로 

nbextensions 탭이 생성되지 않아서 나는 이것이 안 실행된줄알았다. 

그러나

http://localhost:8888/nbextensions?nbextension=nbextensions_configurator/tree_tab/main

이렇게 enable되어 있었고, Tab이 안보이면 아래 처럼 들어가면 

http://localhost:8888/nbextensions

실행되어있다는 것을 확인 할 수 있다. 

위의 링크에서 "?"뒤의 내용은 nbextensions 의 require path 이다. 혹시 이 개념이 나오면 저 내용을 쓰면 될 것 이다. 

자세한 내용은 아래의 링크에서 더 확인 할 수 있겠다. 

[jupyter_contrib_nbextensions github](https://github.com/ipython-contrib/jupyter_contrib_nbextensions)

[nbextensions configurator github](https://github.com/Jupyter-contrib/jupyter_nbextensions_configurator)

