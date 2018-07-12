## Github에 100MB 이상의 파일을 올리는 방법

### 이것은 이 [링크](https://medium.com/@stargt/github%EC%97%90-100mb-%EC%9D%B4%EC%83%81%EC%9D%98-%ED%8C%8C%EC%9D%BC%EC%9D%84-%EC%98%AC%EB%A6%AC%EB%8A%94-%EB%B0%A9%EB%B2%95-9d9e6e3b94ef)의 게시물입니다. 

Bitbucket과는 달리 Github에는 기본적으로 100MB 이상의 파일을 올릴 수 없다.

> Conditions for large files — User Documentation
> <https://help.github.com/articles/conditions-for-large-files/>

그래서 100MB보다 큰 크기의 파일을 올리려고 시도하면 다음과 같은 경고 메시지를 보게 된다.

```
$ git push
Counting objects: 3086, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (2980/2980), done.
Writing objects: 100% (3086/3086), 363.25 MiB | 935.00 KiB/s, done.
Total 3086 (delta 1236), reused 111 (delta 57)
remote: error: GH001: Large files detected. You may want to try Git Large File Storage — https://git-lfs.github.com.
remote: error: Trace: ***
remote: error: See http://git.io/iEPt8g for more information.
remote: error: File *** is 120.94 MB; this exceeds GitHub’s file size limit of 100.00 MB
To git@github.com:***
 ! [remote rejected] master -> master (pre-receive hook declined)
 ! [remote rejected] *** -> *** (pre-receive hook declined)
error: failed to push some refs to ‘git@github.com:***’
```

HEAD의 마지막 Commit에는 100MB가 넘는 파일이 없더라도 이전 Commit 중에 100MB 이상의 파일이 포함된 적이 있다면 이 경고를 피할 수 없다. 그러다 보니 게임과 같이 대용량의 Binary 파일을 자주 다루는 프로젝트를 Github에 올릴 때에는 높은 확률로 위 메시지를 만나게 된다.

### 해결책

다행히도 해결책이 존재한다. 경고 메시지에도 안내되어 있듯이 몇 가지 조처를 해주면 100MB 이상의 파일도 Github에 올릴 수 있다.

#### 1. git-lfs 적용

Commit 과정에서 지정한 파일을 작게 조각내주는 Git extension인 git-lfs — *Git Large File Storage* [*https://git-lfs.github.com/*](https://git-lfs.github.com/) — 를 로컬에 설치한 뒤, 적용하려는 Repository 경로에서 다음 명령을 실행한다.

```
$ git lfs install
Updated pre-push hook.
Git LFS initialized.
```

그다음 용량이 큰 파일을 git-lfs의 관리 대상으로 등록해준다. 다음 예시는 120MB 정도의 exe 파일을 Stage에 추가한 상황에서, 확장자가 exe인 모든 파일을 git-lfs의 관리 대상으로 지정하고 Commit을 수행한 모습이다.

```
$ git lfs track “*.exe”
Tracking *.exe
```

```
$ git commit -m “Large file included”
[master (root-commit) dd2b715] Large file included
(...)
```

이제 하단에 있는 3번 과정대로 Github에 push를 시도하면 된다. 그런데 기존에 100MB 이상의 파일을 Commit한 적이 있다면 여전히 100MB 이상의 파일을 올릴 수 없다는 경고 메시지를 보게 된다. 그럴 땐 다음 2번 과정을 적용해야 한다.

#### 2. BFG Repo-Cleaner 적용

기존 Commit에서 100MB보다 큰 파일의 로그를 강제로 없애줘야 한다. BFG Repo-Cleaner — BFG Repo-Cleaner <https://rtyley.github.io/bfg-repo-cleaner/> — 를 이용하면 그 작업을 손쉽게 적용할 수 있다.

공식 사이트에서 bfq-x.x.x.jar — x.x.x는 버전 — 를 받고, 대상이 되는 Repository에서 다음과 같이 그동안의 Commit에 포함된 100MB 이상의 파일을 정리하는 명령을 실행한다.

```
$ java -jar bfg-x.x.x.jar --strip-blobs-bigger-than 100M
(...)
Deleted files
    — — — — — — -
    Filename Git id
    — — — — — — — — — — — — — — 
    ***.exe | c304fcfb (120.9 MB)
(...)
```

간혹 다음과 같은 오류가 나타날 수 있다.

```
$ java -jar bfg-x.x.x.jar --strip-blobs-bigger-than 100M
```

```
Using repo : C:\***\.git
```

```
Scanning packfile for large blobs: 132
Scanning packfile for large blobs completed in 13 ms.
Warning : no large blobs matching criteria found in packfiles — does the repo need to be packed?
Please specify tasks for The BFG :
bfg x.x.x
(...)
```

그럴 땐 아래 명령을 먼저 수행하고 다시 위의 bfg-x.x.x.jar에 의한 명령을 실행한다.

```
$ git repack && git gc
Counting objects: 3002, done.
(...)
```

#### 3. git-push 재시도

위 과정들을 적용한 뒤 push를 시도하면 다음과 같이 성공 메시지를 볼 수 있다.

```
$ git push
Counting objects: 3089, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (1809/1809), done.
Writing objects: 100% (3089/3089), 234.95 MiB | 1.30 MiB/s, done.
Total 3089 (delta 1236), reused 2890 (delta 1229)
To git@github.com:***
 * [new branch] master -> master
 * [new branch] *** -> ***
```

 