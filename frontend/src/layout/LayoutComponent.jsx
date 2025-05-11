import React, { useState } from 'react';
import { Outlet, useNavigate } from 'react-router-dom';
import { Layout, Menu } from 'antd';
import { ToolOutlined, ShoppingOutlined } from '@ant-design/icons';
import { COLORS } from '../styles/theme';

const { Header, Content } = Layout;

const appStyle = {
  fontFamily: 'Roboto, sans-serif',
  color: COLORS.secondary,
  backgroundColor: COLORS.lightBg,
  minHeight: '100vh',
  minWidth:"100vw"
};

const headerStyle = {
  backgroundColor: COLORS.primaryDark,
  padding: '0 20px',
  boxShadow: '0 2px 8px rgba(0, 0, 0, 0.1)',
};

const menuStyle = {
  backgroundColor: COLORS.primaryDark,
  color: COLORS.white,
};

const menuItemStyle = {
  color: COLORS.white,
  fontSize: '16px',
};

const contentStyle = {
  padding: '48px',
  margin: '48px',
  backgroundColor: COLORS.white,
  borderRadius: '8px',
  boxShadow: '0 2px 8px rgba(0, 0, 0, 0.1)',
};

export default function LayoutComponent() {
  const navigate = useNavigate();
  const [currentPage, setCurrentPage] = useState('materiaprima-cadastro');

  const handleMenuClick = (e) => {
    setCurrentPage(e.key);
    navigate(`/${e.key}`);
  };

  return (
    <Layout style={appStyle}>
      <Header style={headerStyle}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div style={{ color: COLORS.white, fontSize: '20px', fontWeight: 'bold' }}>
            Sistema de Produção
          </div>
          <Menu
            mode="horizontal"
            selectedKeys={[currentPage]}
            onClick={handleMenuClick}
            style={menuStyle}
          >
            <Menu.Item key="materiaprima-cadastro" icon={<ToolOutlined />} style={menuItemStyle}>
              Cadastro de Matérias-Primas
            </Menu.Item>
            <Menu.Item key="producao-iniciar" icon={<ShoppingOutlined />} style={menuItemStyle}>
              Início de Produção
            </Menu.Item>
            <Menu.Item key="placeholder" disabled style={{ visibility: 'hidden' }}>
              Futuras Opções
            </Menu.Item>
          </Menu>
        </div>
      </Header>
      <Content>
        <div style={contentStyle}>
          <Outlet />
        </div>
      </Content>
    </Layout>
  );
}
