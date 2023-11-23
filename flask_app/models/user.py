from flask_app.config.mysqlconnection import connectToMySQL


class User:
    def __init__(self,data):
        self.id = data['id']
        self.full_name = data['full_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users 
    

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (full_name,email, created_at) VALUES(%(full_name)s,%(email)s, NOW());"
        # if u want to get current date add NOW() to appropriate spot needed
        #  but if u want to get updated at u co
        
        results = connectToMySQL('users_schema').query_db(query,data)
        return results
    
    @classmethod
    def get_by_id(cls,id):
        query = """SELECT * FROM users 
        WHERE id= %(id)s"""
        results = connectToMySQL('users_schema').query_db(query,{"id":id})
        return cls(results[0])
    

    @classmethod
    def update(cls,data):
        query = """UPDATE users SET full_name = %(full_name)s,email = %(email)s,updated_at= NOW() 
        WHERE id = %(id)s;""" 
        
        var=connectToMySQL('users_schema').query_db(query,data)
        print(var)
        return var
    
    # Crud - Read
    # the get_one method will be used when we need to retrieve just one specific row of the table
    
    @classmethod
    def delete(cls, user_id):
        query = """DELETE FROM  users 
        WHERE id = %(id)s;"""
        data = {"id": user_id}
        return connectToMySQL('users_schema').query_db(query,data)