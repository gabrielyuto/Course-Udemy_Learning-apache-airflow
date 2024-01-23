# Informações
- Curso: "Domine Apache Airflow: Pipelines de Engenharia de Dados"
- Professor: Fernando Amaral
- Plataforma: Udemy
- Disponível em: https://www.udemy.com/course/domine-apache-airflow/

# Apache Airflow
Apache Airflow é uma plataforma de gerenciamento de fluxo de trabalho de código aberto para pipelines de engenharia de dados. Começou no Airbnb em outubro de 2014 como uma solução para gerenciar os fluxos de trabalho cada vez mais complexos da empresa. A criação do Airflow permitiu que o Airbnb criasse e agendasse programaticamente seus fluxos de trabalho e os monitorasse por meio da interface de usuário integrada do Airflow . Desde o início, o projeto foi tornado de código aberto, tornando-se um projeto Apache Incubator em março de 2016 e um projeto de nível superior da Apache Software Foundation em janeiro de 2019.

O Airflow é escrito em Python e os fluxos de trabalho são criados por meio de scripts Python. O Airflow foi projetado sob o princípio de "configuração como código". Embora existam outras plataformas de fluxo de trabalho de "configuração como código" usando linguagens de marcação como XML , o uso de Python permite que os desenvolvedores importem bibliotecas e classes para ajudá-los a criar seus fluxos de trabalho.

### Principais operadores:
- BashOperator: Executa um comando de shell ou script.
- PythonOperator: executa uma função Python.
- DummyOperator: não faz nada e é útil para fins de organização.
- EmailOperator: envia um email.
- SQLOperator: executa uma consulta SQL.
- FileSensor: aguarda até que um arquivo seja criado ou modificado.
- HttpSensor: aguarda até que uma solicitação HTTP seja bem sucedida.
- TriggerDagRunOperator: executa uma DAG de outra DAG.

### Trigger Rule:
- all_success: se todas as tarefas anteriores foram concluídas com sucesso. 
- all_failed: se todas as tarefas anteriores falharam.
- all_done: quando todas as tarefas anteriores foram concluídas, independentemente do status.
- one_success: se pelo menos uma das tarefas anteriores foi concluída com sucesso.
- one_failed: se pelo menos uma das tarefas anteriores falhou.
- none_failed: se nenhuma das tarefas anteriores falhou.
- none_skipped: se nenhuma das tarefas anteriores foi pulada.
- dummy: a tarefa é sempre executada, independentemente do status das tarefas anteriores.

### Parâmetros de uma Dag
- dag_id: um identificador único para a DAG na cluster.
- description: descrição da DAG.
- schedule_interval: o intervalo de tempo no qual a DAG será executada.
- start_date: a data e hora em que a DAG deve começar a ser executada.
- end_date: a data e hora em que a DAG não deve mais seer executada.
- catchup: determina se a DAG deve executar todas as tarefas que deveriam ter sido executadas desde a data de start_date até o momento atual. Padrão é true.
- default_view: visualização padrão da interface do Airflow para esta DAG. Por exemplo, "graph".
- max_active_runs: máximo de execuções ativas da DAS permitidas.

### Parâmetros de uma DAG
- concurrency: máximo de tarefas que podem ser executadas simultaneamente.
- tags: uma lista de tags para marcar a DAG e suas exceeções.
- default_args: dicionário de argumentos padrão que serão aplicados a todas as tarefas da DAG, a menos que sejam especificamente  substituídos.
- depends_on_past: só inicia se no passado executou com sucesso. Padrão true.
- email: endereço de email para failure ou retry.
- email_on_failure: True/ False.
- email_on_retry: True/ False.
- retries: número padrão de novas tentativas.
- retry_delay: timedelta(minutes=5).


### Schedule_interval
- None
- @once
- @yearly
- @annually
- @monthlyå
- @weekly
- @daily
- @hourly

### xcom: troca de dados entre as tasks
- ti (task instance): é um objeto que representa a instância da tarefa sendo executada.
- xcom_push(): é usada para definir o valor.
- xcom_pull(): é usada para recuperar o valor. 

### Variáveis:
- Permitem armazenar e compartilhar informações entre DAGs.
- Pode ser criada na UI ou na CLI

### Variáveis VS XCom:
- Variáveis: Informações estáticas e globais, usadas em todo o pipeline.
- XCom: Informações dinâmicas; entre as tarefas.

### Pools
- Os pools são usados para gerenciar a concorrência e a alocação de recursos.
- Exemplo: várias tarefas que precisam acessar o banco de dados.

### Branchs
- Muito comum um pipeline precisar seguir em direções diferentes de acordo com resultado de eventos:
- - Caminhos para dados válidos e inválidos
- - Diferentes testes de qualidade
- - Encaminhar diferentes e-mails conforme o resultado da análise
- - etc.

### PythonOperator
- Permite adicionar qualquer funcionalidade Python ao Airflow.
- - Limpeza e tratamento de dados.
- - Transformações, resumos.
- - Extração de fontes diversas.
- - Machine Learning

### Datasets
- Agendamento baseado em uma tarefa que atualiza um dataset
- Dag Producer: atualiza dados
- Dag Consumer: schedule=Dataset

### Sensors
- Aguarda um evento ou disponibilidade de um serviço.
- Não executa nenhuma ação adicional. Por exemplo, verifica arquivo e outra task importa.

#### Principais
1. FileSensor: aguarda a existência ou a ausência de um arquivo em um caminho específico.
2. HttpSensor: aguarda a disponibilidade de uma URL.
3. S3KeySe[Title](http://localhost:8080/home)nsor: aguarda a existência ou a ausência de uma chave em um bucket S3.
4. SqlSensor: aguarda a execução de uma consulta SQL em um banco de dados.

#### Parametros
1. poke_interval: define o intervalo de tempo entre as verificações do sensor.
2. timeout: define o tempo máximo que o sensor pode esperar antes de atingir o tempo limite.
3. soft_fail: especifica se o sensor deve falhar silenciosamente (retornando "False") ou gerar uma exceção quando atinge o tempo limite.
4. mode: especifica o modo de operação do sensor ("reschedule" para agendar novamente a tarefa ou "poke" para continuar verificando até que a condição seja atendida).
5. poke_on_failure: especifica se o sensor deve continuar verificando quando ocorre uma falha na verificação anterior.

### Providers
- Modulos Python que estendem a funcionalidade do Airflow
- Vários tipos: operators, sensors, hooks, etc.
- Muitos já fazem parte do Airflow.
- Podem ser instalados com PIP.
- Exemplos: 
- - apache-airflow-providers-postgres
- - apache-airflow-providers-amazon
- - apache-airflow-providers-google


### Hooks
- Para interação com sistemas externos, como Banco de dados.
- Componentes de Baixo Nível: Mais complexidade, mais flexibilidade, controle granular.
- Hooks são classes e não tasks!
- PostgresOperator: encapsula o PostgresHook com pouquíssimo código.

### Principais comandos para CLI
- airflow dags list -> listar dags
- airflow dags report -> lista as dags 
- airflow dags list-jobs -> listar jobs
- airflow dags next-execution <nome dag> -> mostra a próxima execução da dag
- airflow dags list-runs -d <nome dag> -> lista as execuções da dag
- airflow dags unpause <nome dag> -> controla se a dag fica ou nao pausada
- airflow dags trigger <nome dag> -> dispara uma dag.
- airflow tasks list <nome dag> -> lista as tasks de uma dag.
- airflow tasks test <nome dag> <nome task> <data> -> testar uma task da dag.
- airflow config list -> lista as configurações.
- airflow pools list -> listar os pools
- airflow connections list -> lista as conexões.
- airflow variables list -> lista as variáveis.
- airflow cheat-sheet -> mostrar todos os principais comandos.

### Configurações
- Arquivo airflow.cfg
- docker-compose.yaml: "sobreescreve" airflow.cfg
- Dividido em seções: core, webserver, scheduler.

### Executers
- Alocação de recursos: como e onde executar tarefas
- Gerencia paralelismo
- Gerencia dependências
- Tratamento de falhas
- Monitoramento, logs

#### Tipos
- CeleryExecutor: Execução distribuída em cluster
- SequentialExecutor: Permite apenas execução sequencial
- LocalExecuter: Permite execução em paralelo, mas somente local
- KubernetesExecutor: Executa em ambientes Kubernetes


### Plugins
- Estende a funcionalidade do Airflow
- Pode encapsular código para reutilização
- Classe Python.
- Construtor que herda BaseOperator
- Método Execute.


### PROJETO FINAL

/Users/gabrielyuto/Desktop/projeto.png
