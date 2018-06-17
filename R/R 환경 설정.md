# R 환경 설정 

`Conda 를 이용해서 설치 했을 때, 커널이 바로 죽는 현상이 발생했다.`

이를 해결하기 위해, R의 환경을 따로 만들었고, 안에 jupyter notebook 을 설치 했다.  

현재 내 로컬의 virtualenv환경 중 Python_analysis 에 condaenv 인 R-Env를 설정 했다. 

R을 사용 할 때는 `source activate R-Env ` 로 R-Env 환경을 활성화 시켜서 작업하면 되고, 이 때  Jupyter Notebook의 default port는 8889이다. `https://localhost:8889/tree` 

