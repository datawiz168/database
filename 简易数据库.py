# 定义一个模拟简单数据库的类
class SimpleDatabase:
    # 初始化方法：当创建一个新的数据库实例时会被调用
    def __init__(self):
        # 初始化一个字典来存储数据库的所有表
        self.tables = {}
        
    # 创建新表的方法，接受表名和列名列表作为参数
    def create_table(self, table_name, columns):
        # 检查所给的表名是否已经存在
        if table_name not in self.tables:
            # 如果不存在，则为这个表名在字典中创建一个新的键，并将值设置为一个空列表
            self.tables[table_name] = []
            # 将列名存储在一个实例变量中
            self.columns = columns
        else:
            # 如果表名已存在，则打印一个提示消息
            print(f"Table {table_name} already exists!")
    
    # 插入数据的方法，接受表名和数据（作为字典）作为参数
    def insert(self, table_name, data):
        # 检查所给的表名是否存在
        if table_name in self.tables:
            # 检查要插入的数据的列是否与表的列匹配
            if set(data.keys()) == set(self.columns):
                # 如果匹配，将数据添加到表中
                self.tables[table_name].append(data)
            else:
                # 如果不匹配，则打印一个提示消息
                print("Data columns don't match table columns!")
        else:
            # 如果表不存在，则打印一个提示消息
            print(f"Table {table_name} doesn't exist!")
    
    # 查询数据的方法，接受表名和一个可选的过滤函数作为参数
    def query(self, table_name, filter_func=None):
        # 检查所给的表名是否存在
        if table_name in self.tables:
            # 检查是否提供了过滤函数
            if filter_func:
                # 如果提供了过滤函数，返回满足该函数条件的所有行
                return [row for row in self.tables[table_name] if filter_func(row)]
            else:
                # 如果没有提供过滤函数，返回表中的所有行
                return self.tables[table_name]
        else:
            # 如果表不存在，打印一个提示消息
            print(f"Table {table_name} doesn't exist!")

# 使用示例

# 1. 创建数据库实例
db = SimpleDatabase()

# 2. 创建一个名为'users'的表，有'name'和'age'两列
db.create_table("users", ["name", "age"])

# 3. 向'users'表中插入数据
db.insert("users", {"name": "Alice", "age": 30})
db.insert("users", {"name": "Bob", "age": 25})

# 4. 查询'users'表中所有的数据
print(db.query("users"))

# 5. 查询'users'表中年龄大于28的所有数据
print(db.query("users", filter_func=lambda x: x["age"] > 28))

