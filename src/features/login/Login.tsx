import { useState } from 'react';
import { InputGroup, LoginContainer, StyledButton, StyledInput } from './Login.styles';

function Login() {
  const [idInput, setIdInput] = useState('');
  const [pwdInput, setPwdInput] = useState('');

  const onClick = () => {
    console.log('아이디:', idInput, '비밀번호:', pwdInput);
  };
  return (
    <LoginContainer>
      <h1>로그인</h1>
      <InputGroup>
        <StyledInput
          value={idInput}
          onChange={(event) => setIdInput(event.target.value)}
          className='id-input'
          placeholder='아이디를 입력하세요'
        />
        <StyledInput
          type='password'
          value={pwdInput}
          onChange={(event) => setPwdInput(event.target.value)}
          className='pwd-input'
          placeholder='비밀번호를 입력하세요'
        />
        <StyledButton onClick={onClick}>로그인</StyledButton>
      </InputGroup>
    </LoginContainer>
  );
}

export default Login;
