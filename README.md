# ownbot
Self-hosted [owncast](https://github.com/owncast/owncast) 챗봇 및 매니저봇.  
A self-hosted chat bot &amp; automatic moderator for [owncast](https://github.com/owncast/owncast).

### To-do
#### 명령어
- [ ] 특정 텍스트를 출력하는 명령어 (등록 및 삭제, 사용 권한) - 빵떡 기준 like !명령어 등록 [name] [content], !명령어 삭제 [name], !명령어 정보 (명령어 정보를 볼 수 있음) - commands/config.yml 로드와 command로 custom 확장. __init__() 이용.
- [ ] 특정 시간 간격으로 출력하는 명령어 (타이머) - 빵떡 기준 like !타이머 등록 [name] [interval] [content], !타이머 삭제 [name], !타이머 정보
- [ ] Stream Title 변경 명령어 - 빵떡기준 !방제변경 [stream title] - commands/setStreamTitle.py
- [ ] 음악 신청곡 등록 및 취소, 리스트 (Youtube 기준), 현재 곡과 링크
- [ ] 업타임
- [ ] 방송일정
- [ ] 자동인사
- [ ] 출석체크

#### 매니저 / Moderator
- [ ] 채팅 쿨타임
- [ ] 유저 ban, unban
- [ ] 채팅 slow 모드 (쿨타임 연동)
- [ ] 채팅 청소 (clear)
- [ ] 채팅 금지 (특정 유저, 전체)
- [ ] 금지 단어 차단
- [ ] 이모티콘 도배 차단
- [ ] 특수문자 도배 차단
- [ ] 도배 차단 (같은 말 반복?)
- [ ] 링크 차단 (링크 입력 차단)

#### 후원 / Donation
- [ ] 일반 후원 알림
- [ ] 영상 후원 지원
- [ ] 스티키밤과 유사한 방해 기능
