import mysql.connector


def query_to_js(columns_names, queries):
    query_json = []
    for j in range(len(queries)):
        query_json.append({})
        for i in range(len(columns_names)):
            # if query_json[j]=={}:
            query_json[-1][columns_names[i]] = queries[j][i]

        # query_json.append()
    return query_json


# print(query_to_js(["id", "name", "phone", "roll", "isManager"], workers_query()))


def workers_query():
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user="root",
        password="NadavD3203",
        database="Katsa",
        auth_plugin='mysql_native_password'
    )
    mycursor = mydb.cursor()
    mycursor.execute("""SELECT * from Worker""")
    myresult = mycursor.fetchall()
    print(myresult)
    return query_to_js(["id", "name", "phone", "class", "isManager", "avatar", "isActive"], myresult)


def projects_query():
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user="root",
        password="NadavD3203",
        database="Katsa",
        auth_plugin='mysql_native_password'
    )
    mycursor = mydb.cursor()
    # sql = """SELECT  Project.id, Project.name, Contractor.name,Supervisor.name, Project.location, Project.inactive from Project
    #     inner join Contractor on Contractor.id=Project.contractorId
    #     inner join Supervisor on Supervisor.id=Project.supervisorId
    #     where Project.inactive=1"""
    sql = """select * from project"""
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    # print(query_to_js(["id", "name", "contractorName", "supervisorName", "location"], myresult))
    return query_to_js(
        ["id", "name", "contractorName", "supervisorName", "location", "description", "Tool", "inactive"], myresult)


def insert_newProject(name, contractorName, supervisorName, location, description,Tool):
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user="root",
        password="NadavD3203",
        database="Katsa",
        auth_plugin='mysql_native_password'
    )
    mycursor = mydb.cursor()
    # sql = f"""INSERT INTO Project (name, contractorId, supervisorId, location, inactive) VALUES
    # ('{str(name)}',(select id from Contractor where name='{str(constractorName)}'),
    # (select id from Supervisor where name='{str(supervisorName)}'),'{str(location)}',1)"""
    sql = f"""INSERT INTO Project (name, contractorName, supervisorName, location,description,Tool, inactive) VALUES
     ('{str(name)}','{str(contractorName)}','{str(supervisorName)}','{str(location)}','{str(description)}','{str(Tool)}',1) """
    # print(sql)
    # mycursor.execute(f)
    # print(sql)
    # print(sql)
    mycursor.execute(sql)
    mydb.commit()
    # mycursor.close()
    # mydb.close()


def users_login(name, id):
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user="root",
        password="NadavD3203",
        database="Katsa",
        auth_plugin='mysql_native_password'
    )
    mycursor = mydb.cursor()
    sql = f"""select id,name,avatar,isManager,isActive from Worker where id={id} and name='{name}'"""
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    # print(myresult)
    return query_to_js(['id', 'name', 'avatar', 'isManager', 'isActive'], myresult)
    # myresult = mycursor.fetchall()


# where inactive=1
def risks_query():
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user="root",
        password="NadavD3203",
        database="Katsa",
        auth_plugin='mysql_native_password'
    )
    mycursor = mydb.cursor()
    mycursor.execute("""SELECT * from risk """)
    myresult = mycursor.fetchall()
    # print(myresult)
    return query_to_js(["id", "name", "inactive"], myresult)


# print(workers_query(mydb))


def project_risk_query():
    # mydb = mysql.connector.connect(
    #     host='127.0.0.1',
    #     user="root",
    #     password="NadavD3203",
    #     database="Katsa",
    #     auth_plugin='mysql_native_password'
    # )
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user="root",
        password="NadavD3203",
        database="Katsa",
        auth_plugin='mysql_native_password'
    )
    mycursor = mydb.cursor()
    mycursor.execute("""SELECT ProjectRisk.id,Project.id,Risk.name as riskname, ProjectRisk.inactive FROM ProjectRisk 
    inner join Project on Project.id=ProjectRisk.ProjectId inner join Risk on Risk.id=ProjectRisk.RiskId""")

    myresult = mycursor.fetchall()
    # print(myresult)
    return query_to_js(["id", "projectId", "RiskName", "inactive"], myresult)


def delete_project_risk(id):
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user="root",
        password="NadavD3203",
        database="Katsa",
        auth_plugin='mysql_native_password'
    )
    mycursor = mydb.cursor()
    sql = f"""UPDATE ProjectRisk
        SET inactive=0
        WHERE id={id};"""
    mycursor.execute(sql)
    mydb.commit()
    # print(myresult)


# mydb,

def insert_riskProject(projectid, riskname):
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user="root",
        password="NadavD3203",
        database="Katsa",
        auth_plugin='mysql_native_password'
    )
    mycursor = mydb.cursor()
    sql = f"""INSERT INTO ProjectRisk (projectId, RiskId,inactive) VALUES
        ({projectid},(select id from Risk where name='{str(riskname)}' and inactive=1),1)"""
    print(sql)
    mycursor.execute(sql)
    mydb.commit()


# DELETE FROM table_name WHERE condition mydb,
def newRisk(riskname):
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user="root",
        password="NadavD3203",
        database="Katsa",
        auth_plugin='mysql_native_password'
    )
    print(riskname)
    mycursor = mydb.cursor()
    sql = f"""INSERT INTO Risk (name, inactive) VALUES
        ('{str(riskname)}', 1)"""
    print(sql)
    mycursor.execute(sql)
    mydb.commit()


# SELECT Comment.id,Comment.description,worker.name as workername, Project.name as projectname, Risk.name as riskname
# FROM Comment inner join Worker on Worker.id=Comment.workerId inner join ProjectRisk
# on ProjectRisk.id=Comment.ProjectRiskId inner join Project on Project.id=ProjectRisk.ProjectId
# inner join risk on Risk.id=ProjectRisk.RiskId
def comment():
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user="root",
        password="NadavD3203",
        database="Katsa",
        auth_plugin='mysql_native_password'
    )
    mycursor = mydb.cursor()
    # sql = f"""SELECT Comment.id,Comment.description,worker.name as workerName, Project.name as projectName,
    # Risk.name as riskName
    #             FROM Comment inner join Worker on Worker.id=Comment.workerId inner join ProjectRisk
    #             on ProjectRisk.id=Comment.ProjectRiskId inner join Project on Project.id=ProjectRisk.ProjectId
    #             inner join risk on Risk.id=ProjectRisk.RiskId"""'projectId', 'riskId',Project.id as projectId, Risk.id
    #             as riskId,inner join Project on Project.id=ProjectRisk.ProjectId
    #                 inner join risk on Risk.id=ProjectRisk.RiskId

    sql = f"""SELECT Comment.id,Comment.description,worker.name as workerName, Comment.date, comment.ProjectRiskId,
                worker.avatar,comment.inactive
                FROM Comment inner join Worker on Worker.id=Comment.workerId inner join ProjectRisk
                on ProjectRisk.id=Comment.ProjectRiskId  ORDER BY date ASC"""

    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return query_to_js(['id', 'description', 'workerName', 'date', 'ProjectRiskId', 'avatar', 'inactive'], myresult)


def insert_comment(projectRiskId, description, workerName):
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user="root",
        password="NadavD3203",
        database="Katsa",
        auth_plugin='mysql_native_password'
    )
    mycursor = mydb.cursor()
    sql = f"""INSERT INTO comment (projectRiskId, description,workerId, inactive) VALUES
        ({projectRiskId},'{description}',(select id from Worker where name='{str(workerName)}'),1)"""

    mycursor.execute(sql)
    mydb.commit()


def update_comment(body, id):
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user="root",
        password="NadavD3203",
        database="Katsa",
        auth_plugin='mysql_native_password'
    )
    mycursor = mydb.cursor()
    sql = f"""UPDATE comment
        SET description='{body}'
        WHERE id={id};"""

    mycursor.execute(sql)
    mydb.commit()


def Delete_comment(id):
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user="root",
        password="NadavD3203",
        database="Katsa",
        auth_plugin='mysql_native_password'
    )
    print(1)
    mycursor = mydb.cursor()
    sql = f"""UPDATE comment
        SET inactive=0
        WHERE id={id};"""
    print(sql)
    mycursor.execute(sql)
    mydb.commit()


def Delete_worker(id):
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user="root",
        password="NadavD3203",
        database="Katsa",
        auth_plugin='mysql_native_password'
    )
    print(1)
    mycursor = mydb.cursor()
    sql = f"""UPDATE worker
            SET isActive=0
            WHERE id={id};"""
    print(sql)
    mycursor.execute(sql)
    mydb.commit()


def insert_worker(name, id, phoneNumber, Class, profile, manager):
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user="root",
        password="NadavD3203",
        database="Katsa",
        auth_plugin='mysql_native_password'
    )
    # isManager=0
    print(manager)
    if manager == True:
        isManager = 1
    else:
        isManager = 0
    mycursor = mydb.cursor()
    sql = f"""INSERT INTO worker (id,name,phone,Class,avatar,isManager, isActive) VALUES ({id},'{name}', '{phoneNumber}', '{Class}','{profile}',{isManager},1) """
    print(sql)
    mycursor.execute(sql)
    mydb.commit()
