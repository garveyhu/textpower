# TextPower: amplify llm capabilities through langchain

## 🦊 介绍

 一种利用 [langchain](https://github.com/hwchase17/langchain) 思想实现的放大llm能力的应用，用以建立一套对中文场景与开源模型支持友好的llm应用解决方案。

## 🚩 特点

- **配置灵活**：系统、API配置集中管理，支持模型随意切换，不入侵代码。
- **多模型支持**：支持多种llm、embedding模型，包括OpenAI、讯飞星火、百度千帆、阿里通义千问、百川等。
- **IOC设计**：实现IOC机制，统一管理功能组件
- **自动注册路由**：扫描所有router自动注册
- **一键启动**：快速启动项目，一键部署

## 🌟 Quickstart

1. 配置

   复制.env.example修改文件名为.env，添加你的系统设置

   复制config.json.example修改文件名为config.json，添加你的模型设置

2. 启动项目

   ```bash
   # Windows
   .\run.bat 
   # Mac/Linux
   .\run.sh
   ```

## 🐳 Docker 部署

```bash
sudo docker-compose up -d
```

## 🚁 模型支持

### LLM 模型支持

在线 LLM 模型目前已支持的列表如下：

- **OpenAI**
  - `text-davinci-003`
  - `gpt-3.5-turbo`
  - `gpt-3.5-turbo-16k`
  - `gpt-3.5-turbo-1106`
  - `gpt-4`
  - `gpt-4-32k`
  - `gpt-4-turbo-preview`
  - `gpt-3.5-turbo-instruct`

- **讯飞星火**
  - `spark-v2`
  - `spark-v3`
  - `spark-v3.5`

- **百度千帆**
  - `ERNIE-Bot-turbo`
  - `ERNIE-4.0-8K`

- **阿里通义千问**
  - `qwen-turbo`
  - `qwen-plus`

- **百川**
  - `Baichuan2-Turbo-192K`

### Embedding 模型支持

目前已支持的Embedding模型列表如下：

- **OpenAI**
  - `text-embedding-3-large`
  - `text-embedding-3-small`
  - `text-embedding-ada-002`

- **百度千帆**
  - `Embedding-V1`

- **阿里**
  - `text-embedding-v1`

- **百川**
  - `Baichuan-Text-Embedding`