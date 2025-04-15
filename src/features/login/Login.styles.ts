import styled from 'styled-components';

export const LoginContainer = styled.div`
  font-size: 3rem;
  display: flex;
  flex-direction: column; // 주축
  justify-content: center; // 세로 중앙 정렬(항상 주축을 기준으로 정렬함)
  align-items: center; // 가로 중앙 정렬(항상 교차축을 기준으로 정렬한다)
  height: 100vh; // 전체 높이 기준
`;

export const InputGroup = styled.div`
  width: 50%;
  height: 70%;
  display: flex;
  flex-direction: column;
  align-items: center;
`;

export const StyledInput = styled.input`
  width: 100%;
  height: 20%;
  margin: 1rem;
  font-size: 1rem;
`;

export const StyledButton = styled.button`
  width: 50%;
  height: 15%;
  font-size: 1rem;
  border-radius: 1rem;
  background-color: tomato;
  color: white;
`;
