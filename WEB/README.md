1. 데이터 전송 기본 원칙
   프론트엔드와 백엔드 간의 데이터 전송은 기본적으로 문자열 형식으로 이루어짐.
   모든 데이터 타입(숫자, 불리언, 객체 등)은 전송 전에 문자열로 변환해야 함.
2. 형변환
   클라이언트에서:
   숫자: String(someNumber)
   불리언: someBoolean.toString()
   객체: JSON.stringify(someObject)
   서버에서:
   숫자: int(request.data.get('key'))
   불리언: request.data.get('key') == 'true'
   JSON: json.loads(request.data.get('key'))
3. FormData 사용
   FormData를 사용할 경우, 데이터는 키-값 쌍으로 전송되며, 모든 값은 문자열로 처리됨.
   파일 업로드 시, 파일은 바이너리 형식으로 전송되지만 메타데이터는 문자열로 처리됨.
4. 특수한 데이터 처리
   파일: FormData를 통해 업로드 시, 메타데이터와 함께 전송됨.
   null 값 처리:
   클라이언트에서 빈 문자열로 전송하거나 필드를 아예 추가하지 않음.
   서버에서 빈 문자열을 체크하여 None으로 변환.
