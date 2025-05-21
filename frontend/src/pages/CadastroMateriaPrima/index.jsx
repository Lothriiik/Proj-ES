import React, { useState } from 'react';
import { 
  Form, 
  Input, 
  Button, 
  Select, 
  Typography, 
  message, 
  Divider, 
  Result 
} from 'antd';
import { SaveOutlined } from '@ant-design/icons';
import { COLORS, buttonStyle } from '../../styles/theme';
import { cadastrarmateria } from '../../services/materiais'; // 👈 importe aqui

const { Title } = Typography;
const { Option } = Select;
const { TextArea } = Input;

function CadastroMateriaPrima() {
  const [form] = Form.useForm();
  const [submitting, setSubmitting] = useState(false);
  const [success, setSuccess] = useState(false);

  const unidadesMedida = [
  { label: 'Metro', value: 'm' },
  { label: 'Metro Quadrado', value: 'm²' },
  { label: 'Quilo', value: 'kg' },
  { label: 'Grama', value: 'g' },
  { label: 'Litro', value: 'L' },
  { label: 'Unidade', value: 'un' }
];


  const handleSubmit = async (values) => {
  setSubmitting(true);
  try {
    await cadastrarmaterias({
      name: values.name,
      description: values.description,
      unit: values.unit
    });
    message.success('Matéria-prima cadastrada com sucesso!');
    form.resetFields();
  } catch (error) {
    message.error('Erro ao cadastrar matéria-prima.');
  } finally {
    setSubmitting(false);
  }
};


  if (success) {
    return (
      <Result
        status="success"
        title="Matéria-prima cadastrada com sucesso!"
        subTitle="A nova matéria-prima foi adicionada ao estoque."
        extra={[
          <Button 
            type="primary" 
            key="novo" 
            onClick={() => setSuccess(false)}
            style={buttonStyle}
          >
            Cadastrar Nova Matéria-Prima
          </Button>
        ]}
      />
    );
  }

  return (
    <div>
      <Title level={2} style={{ color: COLORS.primaryDark }}>
        Cadastro de Matérias-Primas
      </Title>
      <Divider />
      
      <Form
  form={form}
  layout="vertical"
  onFinish={handleSubmit}
  initialValues={{ unidade_medida: 'un' }}
>
  <Form.Item
    label="Nome"
    name="name"
    rules={[{ required: true, message: 'Por favor, insira o nome!' }]}
  >
    <Input />
  </Form.Item>

  <Form.Item
    label="Descrição"
    name="description"
    rules={[{ required: true, message: 'Por favor, insira a descrição!' }]}
  >
    <Input />
  </Form.Item>

  <Form.Item
    label="Unidade de Medida"
    name="unit"
    rules={[{ required: true, message: 'Selecione uma unidade de medida!' }]}
  >
    <Select>
      {unidadesMedida.map((unidade) => (
        <Select.Option key={unidade.value} value={unidade.value}>
          {unidade.label}
        </Select.Option>
      ))}
    </Select>
  </Form.Item>

  <Form.Item>
    <Button
      type="primary"
      htmlType="submit"
      icon={<SaveOutlined />}
      loading={submitting}
      style={buttonStyle}
      size="large"
    >
      Cadastrar Matéria-Prima
    </Button>
  </Form.Item>
</Form>
    </div>
  );
}

export default CadastroMateriaPrima;
