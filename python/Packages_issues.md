### argparse module

------------

>  ```pip install argparse  ```
>
>  ```import arge parse```



* argparse : 명령어 옵션 설정 - [설정법 링크 참조](https://soooprmx.com/archives/5756)

# argparse

> https://docs.python.org/3/library/argparse.html?highlight=argparse#module-argparse

CLI툴을 만들 때 다양한 옵션 스위치들을 제공하려는 경우, 이를 일일이 파싱하는 것은 사실 쉽지 않다.파이썬에서는 `argparse` 모듈이 이러한 작업을 보다 편하게 할 수 있게 도와준다.

## ArgumentParser

`argparse.ArgumentParser` 클래스는 명령줄 옵션을 파싱하는 객체이다. 별다른 서브클래싱없이 그대로 가져다가 객체를 생성하면 된다. 객체 생성후에는 `add_argument()` 함수를 통해서 각 스위치와 그 옵션들을 추가해주고, 최종적으로 전달된 arguments들을 던져주면 사전형태로 이를 돌려주게 된다.

```
import argparse
parser = argparse.ArgumentParser(description="args parser")
```

## add_argement()

파서객체의 `add_argument()` 메소드는 파라미터 파싱처리의 핵심을 담당한다고 해도 과언이 아니다.

시그니처는 대략 다음과 같다.

```
.add_argument(name or flags...[,action][,nargs][,default][,type][,choices][,required][,help][,metavar][,dest])
```

각 옵션들은 다음과 같은 역할을 한다.

- 우선 한 번에 한 종류의 스위치를 등록할 수 있다.
- `name or flags` : 등록할 파라미터의 이름이나 스위치를 등록한다. “foo”, “-f”, “–foo” 등이 가능하다.
- `action`: 스위치가 주어졌을 때, 표준 동작을 정한다. 기본값은 “store”이고 이는 주어진 스위치의 옵션 값을 플래그(혹은 이름)의 키에 저장한다. 단지 on/off 개념의 스위치라면 `"store_true"`를 줄 수 있다. 또 배열형태로 저장될 복수 사용되는 스위치([[GCC의 ‘-I’ 옵션]] 같은)에는 `"append"`를 줄 수 있다. 개수만 세는 경우 “count”를 줄 수도 있고.
- `nargs` : 스위치나 파라미터가 받을 수 있는 값의 개수를 가리킨다. 이 값보다 많은 값이 들어오는 경우 무시된다. “+”로 설정하는 경우 1개 이상.
- `default`: 뒤에 별도 값이 없는 경우 디폴트로 들어갈 값
- `type`: 파싱하여 저장할 때 타입을 변경할 수 있다.
- `choices`: 리스트 형태로 전달하면, 리스트의 원소와 일치하는 것만 취한다.
- `required`: 필수 파라미터인 경우 True로 설정. 없으면 알아서 에러메시지를 표시하고 자동으로 exit한다.
- `help`: –help 옵션을 받았을 때, 표시될 메시지 목록에서 스위치의 도움말을 설정한다.
- `metavar`: usage 메시지를 출력할 때 표시할 메타변수이름을 지정해준다.
- `dest` : 스위치나 파라미터이름이 아닌 별도의 변수를 지정할 때 쓴다. 외부에서 변수를 미리 선언한 경우, 해당 변수에 값이 들어간다.

### .parse_args()

각 인자의 리스트를 받아 이를 파싱한 결과를 되돌려 준다. 파싱된 결과는 하나의 네임스페이스를 갖는 객체로 모든 스위치 이름들은 이 객체의 속성 이름으로 정의되어 있다.

만약 인자값을 넘기지 않는다면 기본적으로 `sys.argv`를 사용하게 된다.

------

1. 일련의 문자열을 의미를 가지는 보다 작은 단위로 분해하여 나누는 일. 간단한 파싱의 경우 단순 문자열 치환이나 분해로 가능하지만, 보통의 경우 파서를 제작하는 일은 꽤 어렵다. 명령줄 인자 파싱의 경우에도 오죽하면 C에서도 이를 위한 함수들을 제공하고 있을정도이다! [![↩](https://s.w.org/images/core/emoji/11/svg/21a9.svg)](https://soooprmx.com/archives/5756#fnref-5756-%ED%8C%8C%EC%8B%B1)
2. 정확히는 사전이 아니라, 추가한 argument들을 대상으로 하는 네임스페이스를 구비한 객체를 전달한다. 왜냐하면 동일한 기능을 하는 스위치를 2개 이상의 이름을 줄 수 있기 때문이다. 예를 들어 `-o`와 `--output`은 동일한 스위치로 둘 수 있는데, 이 경우 `args.o` 나 `args.output` 둘 모두로 동일한 값에 접근가능하다.

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





### pyenv 다운로드와 초기 설정



> - https://cjh5414.github.io/ubuntu-pyenv-virtualenv/





### GPU on instance 설정

> - https://medium.com/google-cloud/setting-up-tensorflow-gpu-on-google-cloud-instance-with-ubuntu-16-04-53cb6749b527