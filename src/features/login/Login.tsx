// 로그인 컴포넌트
import { useState } from 'react';
import { InputGroup, LoginContainer, StyledButton, StyledForm, StyledInput } from './Login.styles';

function Login() {
  const [idInput, setIdInput] = useState('');
  const [pwdInput, setPwdInput] = useState('');

  // 버튼 클릭 이벤트 리스너
  const onClick = () => {
    console.log('아이디:', idInput, '비밀번호:', pwdInput);
    if (idInput === '테스터') {
      if (pwdInput === '1234') {
        alert('로그인이 성공했습니다.');
      } else {
        alert('비밀번호가 틀렸습니다.');
      }
    } else {
      alert('잘못된 아이디 입니다.');
    }
  };

  return (
    <LoginContainer>
      <h1>로그인</h1>
      <StyledForm
        onSubmit={(event) => {
          event.preventDefault();
          onClick();
        }}
      >
        <InputGroup>
          <StyledInput
            value={idInput}
            onChange={(event) => setIdInput(event.target.value)}
            className='id-input'
            placeholder='아이디를 입력하세요'
            required
          />
          <StyledInput
            type='password'
            value={pwdInput}
            onChange={(event) => setPwdInput(event.target.value)}
            className='pwd-input'
            placeholder='비밀번호를 입력하세요'
            required
          />
          <StyledButton>로그인</StyledButton>
        </InputGroup>
      </StyledForm>
    </LoginContainer>
  );
}

export default Login;
