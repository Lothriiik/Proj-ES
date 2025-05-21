// components/InicioProducao.jsx
import React, { useState, useEffect } from 'react';
import { 
  Form, 
  Button, 
  Select, 
  InputNumber, 
  Typography, 
  message, 
  Table, 
  Divider, 
  Space, 
} from 'antd';
import { CheckCircleOutlined } from '@ant-design/icons';
import { COLORS, buttonStyle } from '../../styles/theme';
import { getSapatos } from '../../services/api';
import { mockData } from '../../mock/mockData';

const { Title } = Typography;
const { Option } = Select;

function IniciarProducao() {
  const [form] = Form.useForm();
  const [sapatos, setSapatos] = useState([]);
  const [materiais, setMateriais] = useState([]);
  const [materiaisNecessarios, setMateriaisNecessarios] = useState([]);
  const [loading, setLoading] = useState(false);
  const [sapSelecionado, setSapSelecionado] = useState(null);
  
  const { sapatos_mock, materiais_mock, materiaisPorSapato } = mockData;
  
  useEffect(() => {
    // Simular carregamento de dados da API
    setLoading(true);
    
    // Na implementação real:
    // getSapatos()
    //   .then(data => setSapatos(data))
    //   .catch(error => message.error('Erro ao carregar produtos: ' + error.message))
    //   .finally(() => setLoading(false));
    
    // Usando dados mockados por enquanto
    setTimeout(() => {
      setSapatos(sapatos_mock);
      setMateriais(materiais_mock);
      setLoading(false);
    }, 1000);
  }, []);
  
  const handleSapatoChange = (value) => {
    setSapSelecionado(value);
    form.setFieldsValue({ quantidade_planejada: 1 });
    calcularMateriaisNecessarios(value, 1);
  };
  
  const handleQuantidadeChange = (value) => {
    if (sapSelecionado && value) {
      calcularMateriaisNecessarios(sapSelecionado, value);
    }
  };
  
  const calcularMateriaisNecessarios = (sapatoId, quantidade) => {
    const materiaisDoSapato = materiaisPorSapato[sapatoId] || [];
    
    const materiaisCalculados = materiaisDoSapato.map(materialSapato => {
      const materialInfo = materiais.find(m => m.id === materialSapato.material_id);
      const quantidadeNecessaria = materialSapato.quantidade_por_unidade * quantidade;
      const disponivel = materialInfo ? materialInfo.quantidade_disponivel : 0;
      const suficiente = disponivel >= quantidadeNecessaria;
      
      return {
        id: materialSapato.id,
        material: materialInfo,
        quantidade_reservada: quantidadeNecessaria,
        quantidade_disponivel: disponivel,
        suficiente: suficiente
      };
    });
    
    setMateriaisNecessarios(materiaisCalculados);
  };
  
  const handleSubmit = (values) => {
    setLoading(true);
    
    // Preparando os dados para envio
    const dadosProducao = {
      sapato_id: values.sapato_id,
      quantidade_planejada: values.quantidade_planejada,
      materiais: materiaisNecessarios.map(m => ({
        id: m.id,
        material_id: m.material.id,
        quantidade_reservada: m.quantidade_reservada
      }))
    };
    
    console.log('Dados da produção para envio:', dadosProducao);
    
    // Simulando envio para API
    setTimeout(() => {
      message.success('Produção iniciada com sucesso!');
      setLoading(false);
      form.resetFields();
      setMateriaisNecessarios([]);
      setSapSelecionado(null);
    }, 1500);
    
    
  };
  
  const columns = [
    {
      title: 'Matéria-Prima',
      dataIndex: ['material', 'nome'],
      key: 'nome',
    },
    {
      title: 'Unidade',
      dataIndex: ['material', 'unidade_medida'],
      key: 'unidade',
    },
    {
      title: 'Quantidade Necessária',
      dataIndex: 'quantidade_reservada',
      key: 'necessaria',
      render: (valor, registro) => `${valor.toFixed(2)} ${registro.material.unidade_medida}`,
    },
    {
      title: 'Disponível',
      dataIndex: 'quantidade_disponivel',
      key: 'disponivel',
      render: (valor, registro) => `${valor.toFixed(2)} ${registro.material.unidade_medida}`,
    },
    {
      title: 'Status',
      key: 'status',

    },
  ];

  return (
    <div>
      <Title level={2} style={{ color: COLORS.primaryDark }}>
        Início de Produção
      </Title>
      <Divider />
      
      <Form
        form={form}
        layout="vertical"
        onFinish={handleSubmit}
      >
        <Form.Item
          name="sapato_id"
          label="Produto a ser produzido"
          rules={[{ required: true, message: 'Por favor, selecione um produto!' }]}
        >
          <Select 
            placeholder="Selecione o produto" 
            loading={loading}
            onChange={handleSapatoChange}
          >
            {sapatos.map(sapato => (
              <Option key={sapato.id} value={sapato.id}>
                {sapato.nome} (Cód: {sapato.codigo})
              </Option>
            ))}
          </Select>
        </Form.Item>
        
        <Form.Item
          name="quantidade_planejada"
          label="Quantidade Planejada"
          rules={[{ required: true, message: 'Por favor, informe a quantidade!' }]}
        >
          <InputNumber
            min={1}
            placeholder="Ex: 100"
            style={{ width: '100%' }}
            onChange={handleQuantidadeChange}
            disabled={!sapSelecionado}
          />
        </Form.Item>
        
        {materiaisNecessarios.length > 0 && (
          <>
            <Divider />
            <Title level={4}>Materiais Necessários</Title>
            
            <Table 
              dataSource={materiaisNecessarios} 
              columns={columns} 
              rowKey="id"
              pagination={false}
            />
            
            <Divider />
            
            <Form.Item>
              <Button
                type="primary"
                htmlType="submit"
                icon={<CheckCircleOutlined />}
                loading={loading}
                style={buttonStyle}
                size="large"
                disabled={materiaisNecessarios.some(m => !m.suficiente)}
              >
                Iniciar Produção
              </Button>
              

            </Form.Item>
          </>
        )}
      </Form>
    </div>
  );
}

export default IniciarProducao;