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

