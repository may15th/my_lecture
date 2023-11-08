js에서 이벤트 다루는 방법, dom 조작

버튼 클릭했을 때 팝업창이 출력되는 것

-> 일상에서의 이벤트처럼 웹에서도 이벤트를 통해 특정 동작 수행한다.

모든 DOM 요소는 이러한 event를 만들어 냄
tag, content, 속성 등

enent object
DOM에서 이벤트가 발생했을 때 생성되는 객체

- 이벤트 종류
js를 통해서 event를 받고 
받은 event를 처리한다. 처리하는 걸 event handeler라고 한다.

dom에서 input event발생하면 그 때 무언가 하겠다는 코드 작성

event handler
이벤트가 발생했을 때 실행되는 함수
->사용자의 행동에 어떻게 반응할지를 js코드로 작성한 것.

(dom).addEventListener()
대표적인 이벤트 핸들러.
->특정 이벤트를 DOM 요소가 수신할 떄마다 콜백 함수 호출

콜백함수 =
어떠한 외부 함수의 인자로 들어가는 함수

for each array help method에서 본격적 학습 햇음..

EventTarget.addEventListener(type, handler)

type = click, ... 등
정해진 이름들이 있어.

대상에 특정 이벤트가 발생하면 
지정한 이벤트(콜백함수)를 받아 할 일을 등록한다.

type
- 수신할 이벤트 이름
- 문자열로 작성 ex.'click'

handler
- 발생한 이벤트 객체를 수신하는 콜백 함수
- 콜백함수는 발생한 event object를 유일한 매개변수로 받음.




