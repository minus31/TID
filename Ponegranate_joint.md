**02.07.03.02 결합 확률과 조건부 확률**  중, 범인 찾기 문제를 예로 들었을 때, 

사건 X : 남자 인지 여자 인지 

사건 Y : 머리가 긴 지 짧은지 

---

이 때, 남자는 12명, 여자는 8명, 머리긴 사람은 10명, 짧은 사람은 10명  (Marginal)

그리고 다음과 같은 경우 일 때, 

["남자", "긴", 3/20],
["남자", "짧은", 9/20],
["여자", "긴", 7/20],
["여자", "짧은", 1/20]

**Ponegranate** 패키지를 이용해서 구현하면 다음과 같이 결합확률 분포를 구현 합니다. 

<img src="https://www.dropbox.com/s/ssr36g5pl22o3g1/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202018-11-28%2015.10.09.png?raw=1">

`JointProbablilityTable()`내에 결합확률 테이블을 입력합니다. **하지만** 이렇게 하면 결합확률을  구해주지 않습니다. 다음은 `JointProbablilityTable()`의 하부 함수인 `.marginal()`의 실행 화면 입니다. 

<img src="https://www.dropbox.com/s/dfi71wjv5uz61g9/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202018-11-28%2015.12.00.png?raw=1">

이 에러를 해결하기 위해서는 다음과 같이 미리 주변 확률 분포에 대한 정보를 `JointProbablilityTable()`를 생성할  때 입력해주어야 합니다. 

<img src="https://www.dropbox.com/s/08qzldvae5ao0d7/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202018-11-28%2015.13.39.png?raw=1">





<img src="https://www.dropbox.com/s/0a56nqasfn8l8tg/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202018-11-28%2015.13.57.png?raw=1">

즉, 미리 주변확률을 정의 하여 입력하지 않으면 결합확률에서 주변확률을 추론할 수 없게 되어 있습니다. 

반면, **pgmpy**의 경우 다음 그림과 같이 구현 했습니다. 

<img src="https://www.dropbox.com/s/ik3esl0g1h4zrkp/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202018-11-28%2014.53.46.png?raw=1" > 

Pgmpy를 이용해 결합확률분포를 만들 때는 주변 확률에 대한 데이터는 입력되지 않았습니다. 그렇지만 다음 과 같이 marginalize, marginal_distribution() 함수로 둘의 주변 확률을 구했습니다. 

<img src="https://www.dropbox.com/s/3naayf8oshebcbr/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202018-11-28%2015.08.05.png?raw=1">



