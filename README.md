# FastAPI 示例应用

![Python versions](https://img.shields.io/badge/python-3.7+-blue?style=flat-square)
![License](https://img.shields.io/github/license/zhengxs2018/fastapi-realworld-example-app?style=flat-square)

使用 Python 3.7+ 和 FastAPI 并基于标准的 Python 类型提示构建 API 的 RealWorld 示例应用。

## 快速开始

推荐使用 [venv](https://docs.python.org/3/library/venv.html) 或 [pyenv](https://github.com/pyenv/pyenv) 启动。

```sh
# 安装依赖
$ pip3 -r requirements.txt

# 启动服务
$ uvicorn app.main:app --port 8080

# 启动服务 (开发模式)
$ uvicorn app.main:app --port 8080 --reload
```

辅助开发工具

```sh
# 安装依赖
$ pip3 install -U black mypy

# 代码美化
$ python3 -m black app

# 类型检查
$ python3 -m mypy app
```

## For VS Code

- [Using Python environments in VS Code](https://code.visualstudio.com/docs/python/environments)
- [借助 Visual Studio Code 将 Docker 容器用作开发环境](https://learn.microsoft.com/zh-cn/training/modules/use-docker-container-dev-env-vs-code/)

## 链接

以下排名不分先后

- [uvicorn](https://www.uvicorn.org)
- [fastapi](https://fastapi.tiangolo.com)
- [black](https://black.readthedocs.io)
- [mypy](http://mypy-lang.org)
- More.

## License

MIT
