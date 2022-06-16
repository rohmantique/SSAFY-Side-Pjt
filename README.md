# 서울1반 추억쌓피





## 개발 기간

2022.04.12 ~ 5.23



## 팀원 및 역할

팀명: 뚱땅즈

FrontEnd: 노희진, 명은호

BackEnd: 김수연, 노희진



## 기술 스택

FrontEnd: JavaScript, HTML, CSS

BackEnd:  Python, Django, SQLite3, AWS





## 협업 툴

Git, Github, MatterMost, Notion, Discord



## 서비스 소개

- ‘먼지 쌓일 일 없고, 잃어버릴 일 없는’ 온라인 롤링 페이퍼 서비스를 기획했습니다.
- 편지쓰기 기간을 정해 모든 사용자가 편지를 쓸 수 있도록 유도했습니다.
- 편지함 공개 날짜를 종강 날짜에 맞춰 '서로의 격려 속에 한 학기를 잘 마무리하자'는 의미를 더했습니다.



## ERD



![ddoongddang_erd](서울1반_추억쌓피_회고.assets/ddoongddang_erd.png)



## 주요 기능



#### User

- 회원가입 시 아이디와 닉네임 정규표현식 조건 부여
- 회원가입 시 아이디, 닉네임 중복 검사
- 지정 사용자 이외엔 회원가입 불가능
- 아이디 및 비밀번호 분실 시 사용자 이메일로 재설정 링크 전송

#### RollPaper

- 지정 날짜 이전에는 편지 작성/수정/삭제만 가능
- 지정 날짜 이후에는 편지 조회만 가능
- 탈퇴한 사용자의 편지 정보 DB에 남기기
- 사용자에게 미리 받은 설문 결과로 워드 클라우드 이미지 생성 후, 편지함 화면에 출력





### 서비스 이미지 예시

- 편지 조회, 워드 클라우드 이미지 출력

> 미리 설정해놓은 날짜가 되면 편지함이 공개됩니다. 해당 날짜 이전에는 편지함을 확인할 수 없습니다. 편지함에 워드 클라우드 이미지가 함께 출력됩니다.
>
> <img src="서울1반_추억쌓피_회고.assets/편지확인.gif" alt="편지확인" style="zoom: 50%;" />

  

- 회원 메일을 통한 아이디 (및 비밀번호) 찾기

> 회원 가입 시 사용자로부터 받은 이메일 주소로 사용자의 아이디와 서비스 링크를 함께 보냅니다. 비밀번호 재설정의 경우 재설정 링크를 보냅니다.
>
> <img src="서울1반_추억쌓피_회고.assets/아이디찾기_메일전송성공.gif" alt="아이디찾기_메일전송성공" style="zoom:150%;" />







## 코드에 대하여

- BackEnd: https://better-pint-8a3.notion.site/BE-62fcd8123e034d99b1b50c1c9a120621
- FrontEnd: https://better-pint-8a3.notion.site/FE-c44b45ba916f4ef4b8a95a98796c6744
- 서비스 확장을 위해: https://better-pint-8a3.notion.site/3ef27b2872a74e6a9ade91254839364d



## 성과

- 삼성 청년 SW 아카데미 8기 공식 롤링 페이퍼 서비스로 출시 예정





## Resource

회의록 및 개발 상세 일정표: https://better-pint-8a3.notion.site/s-963d8cd856734b44bdb744856e39fc34



