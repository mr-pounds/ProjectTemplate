# 快速创建项目

开发环境的配置还是有较多内容，为了减少重复工作，需要用到 cookiecutter 进行项目创建。我已经将上述内容整合到项目模板中，执行如下命令可直接创建项目。

```Shell
pip install cookiecutter # 不用安装到虚拟环境
cookiecutter https://e.coding.net/jinuobushibili/zzz_tools/ProjectTemplate.git
```
除上述内容外，项目模板中还包含项目目录、项目配置等多项内容。

# 项目代码结构
* docs(dir)：项目文档库
* template(dir)：模板文件库
* bin(dir)：入口文件，可无
* db(dir)：数据文件地址
* log(dir)：项目日志文件
* conf(dir)：项目配置文件
* tests(dir)：测试代码
* lib(dir)：自定义的模块或包
* sample(dir)：关键代码文件，每个包单独目录
   * \_ *init* \_.py
   * main.py
   * setting.py：添加了部分目录的路径变量，如db。
* README.md：项目说明文档
* requirements.txt：项目依赖的三方库
* setup.py：安装、部署、打包代码

# 修改项目模板
若要基于自己的需求，对项目模板进行修改的话，也是比较简单的。

## 变量修改
cookiecutter变量，通过 cookiecutter.json 进行修改。其中的值为默认值，在创建项目时，会要求再次确认。而变量的使用，只需在对应的文件中，使用 {{ 变量名 }}即可。但需保证文件的编码为utf-8。

## 目录/文件调整
cookiecutter生成的文件目录是{{cookiecutter.project\_slug}}，需要项目自动生成的文件要放到这个目录下。

在{{cookiecutter.project\_slug}}目录下操作即可，对根目录下其他目录的修改是不会影响创建项目的。

## 开发环境调整
调整完以后，记得更新requirem或pipfile即可。相关操作，请查看上方对应内容。

## Hooks
cookiecutter的hooks全部在hooks目录下。

* pre\_gen\_project.py：项目创建前
* post\_gen\_project.py：项目创建后

结合cookiecutter变量与hooks，可以进行许多复杂的操作。我还没怎么用。
