# 정보 discordbot 만들기
- 특정 command 입력하면 hello 출력하기
- MMA API docs :  https://developer.sportradar.com/docs/read/combat_sports/MMA_v2#mma-api-overview

### Step by Step - MMA API
- discord bot 에 들어갈 데이터 가져오기
- 결과값 : 선수 프로필 정보
- 정보 가져오기 : 경기 정보(season info_id) -> 경기한 선수 정보(fighter info_id) -> 선수 프로필 정보

### Step by Step - discord 
#### Step 1. discord bot의 특정 command 를 입력하면 discord 에 원하는 메시지가 출력되기 (1)
- 간단하게 hello command 입력 -> hi 출력
#### Step 2. discord bot 특정 command 를 입력하면 discord 에 원하는 메시지가 출력되기 (2)
-  코드 안에서 설정값을 바꾸면 메시지도 바뀌게 하기. 
-  예. search=jung -> jung 에 대한 메시지 출력 
-  API 와 결합하기

#### Step 4. 특정 command + 사용자 입력값 (2개) 받아 메시지 출력
- 필요한 정보인 선수 이름, 경기명 을 받아 api 에서 선수 프로필 가져오기

#### Step 5. 리팩토링
- API 에서 검색이 안되어 오류나는 경우 "정보가 존재하지 않습니다" 메시지 출력하기
- API 조회 코드를 다른 함수로 분리하기


