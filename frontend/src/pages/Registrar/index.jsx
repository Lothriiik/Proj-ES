import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Form, Input, Button, Modal } from 'antd';
import { cadastrar } from '../../api/main';
import './styles.css';

export default function Registrar() {
  const [loading, setLoading] = useState(false);
  const [isModalVisible, setIsModalVisible] = useState(false);
  const navigate = useNavigate();

  const onFinish = async (values) => {
    const { confirmPassword, ...userData } = values;
    setLoading(true);
    try {
      await cadastrar({ ...userData, role: 'operador' });
      setIsModalVisible(true);  // mostra modal
    } catch (error) {
      Modal.error({
        title: 'Erro',
        content: 'Erro ao registrar usuário. Tente novamente.',
      });
    } finally {
      setLoading(false);
    }
  };

  const handleModalOk = () => {
    setIsModalVisible(false);
    navigate('/login');  // navega ao fechar modal
  };

  return (
    <div className="registrar-container">
      <div className="registrar-card">
        <h2 className="registrar-title">ReTock - Registrar</h2>

        <Form layout="vertical" onFinish={onFinish}>
          <Form.Item
            name="username"
            label="Usuário"
            rules={[{ required: true, message: 'Por favor, insira o nome de usuário' }]}
          >
            <Input placeholder="Digite o nome de usuário" />
          </Form.Item>

          <Form.Item
            name="password"
            label="Senha"
            rules={[{ required: true, message: 'Por favor, insira a senha' }]}
          >
            <Input.Password placeholder="Digite a senha" />
          </Form.Item>

          <Form.Item
            name="confirmPassword"
            label="Confirmar senha"
            dependencies={['password']}
            rules={[
              { required: true, message: 'Por favor, confirme a senha' },
              ({ getFieldValue }) => ({
                validator(_, value) {
                  if (!value || getFieldValue('password') === value) {
                    return Promise.resolve();
                  }
                  return Promise.reject(new Error('As senhas não coincidem'));
                },
              }),
            ]}
          >
            <Input.Password placeholder="Digite novamente a senha" />
          </Form.Item>

          <Form.Item>
            <Button
              className="login-button"
              type="primary"
              htmlType="submit"
              block
              loading={loading}
            >
              Registrar
            </Button>
          </Form.Item>
        </Form>

        <Modal
          title="Sucesso"
          open={isModalVisible} 
          onOk={handleModalOk}
          cancelButtonProps={{ style: { display: 'none' } }}
        >
          <p>Usuário registrado com sucesso!</p>
        </Modal>
      </div>
    </div>
  );
}
