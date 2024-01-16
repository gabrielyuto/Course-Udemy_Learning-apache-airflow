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
- ti (task instance): é um objeto que representa a instância da tarefa sendo executada.å
- xcom_push(): é usada para definir o valor.
- xcom_pull(): é usada para recuperar o valor. 