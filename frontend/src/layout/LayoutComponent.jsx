import React, { useState, useEffect } from 'react';
import { Outlet, useNavigate } from 'react-router-dom';
import { Layout, Menu } from 'antd';
import { ToolOutlined, ShoppingOutlined } from '@ant-design/icons';
import { COLORS } from '../styles/theme';
import './Layout.css'; 

const { Header, Content } = Layout;


const appStyle = {
  fontFamily: 'Roboto, sans-serif',
  color: COLORS.secondary,
  backgroundColor: COLORS.lightBg,
  minHeight: '100vh',
  minWidth: "100vw"
};

const headerStyle = {
  backgroundColor: COLORS.primaryDark,
  padding: '0 20px',
  boxShadow: '0 2px 8px rgba(0, 0, 0, 0.1)',
  
};

const menuStyle = {
  backgroundColor: COLORS.primaryDark,
  color: COLORS.white,
  borderBottom: 'none',
  width:'400px'
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
  const [currentPage, setCurrentPage] = useState('');

  useEffect(() => {
    const styleElement = document.createElement('style');
    styleElement.innerHTML = `
      .ant-menu-dark .ant-menu-submenu-title {
        color: white !important;
      }
      .ant-menu-dark .ant-menu-item:hover {
        background-color: ${COLORS.primaryDark} !important;
      }
      .custom-dropdown {
        background-color: ${COLORS.primaryDark} !important;
      }
      .custom-dropdown .ant-menu-item {
        color: white !important;
      }
    `;
    document.head.appendChild(styleElement);
    
    return () => {
      document.head.removeChild(styleElement);
    };
  }, []);

  const handleMenuClick = (e) => {
    setCurrentPage(e.key);
    navigate(`/${e.key}`);
  };

  return (
    <Layout style={appStyle}>
      <Header style={headerStyle}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div style={{ color: COLORS.white, fontSize: '20px', fontWeight: 'bold' }}>
            ReTock
          </div>
          <Menu
            mode="horizontal"
            selectedKeys={[currentPage]}
            onClick={handleMenuClick}
            style={menuStyle}
            theme="dark"
          >
            <Menu.SubMenu 
              key="producao" 
              icon={<ShoppingOutlined />} 
              title="Produção"
              popupClassName="custom-dropdown"
            >
              <Menu.Item key="producao-criar">Criar</Menu.Item>
              <Menu.Item key="producao-iniciar">Iniciar</Menu.Item>
              <Menu.Item key="producao-visualizar">Visualizar</Menu.Item>
            </Menu.SubMenu>
            
            <Menu.SubMenu 
              key="materiaprima" 
              icon={<ToolOutlined />} 
              title="Matéria Prima"
              popupClassName="custom-dropdown"
            >
              <Menu.Item key="materiaprima-adicionar">Adicionar</Menu.Item>
              <Menu.Item key="materiaprima-visualizar">Visualizar</Menu.Item>
            </Menu.SubMenu>
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