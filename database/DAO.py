from database.DB_connect import DBConnect
from model.states import State


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getYears():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select  DISTINCT (YEAR(`datetime`)) as y
                    from sighting s """
        cursor.execute(query)
        for row in cursor:
            result.append(row["y"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getForma():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select distinct(shape) as s
                    from sighting s """
        cursor.execute(query)
        for row in cursor:
            result.append(row["s"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getState():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT *
                    from state s """
        cursor.execute(query)
        for row in cursor:
            result.append(State(**row))
        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getNeig(idMap):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT *
            from neighbor n """
        cursor.execute(query)
        for row in cursor:
            result.append((idMap[row["state1"]],idMap[row["state2"]]))
        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getPeso(y,sh,n1,n2):
        conn = DBConnect.get_connection()
        result = 0
        cursor = conn.cursor(dictionary=True)
        query = """select s.state,count(*) as c
                    from sighting s 
                    where shape =%s
                    and (state=%s or state=%s)
                    and YEAR(`datetime`)=%s
                    group by state
                     """
        cursor.execute(query, (sh,n1,n2,y,))
        for row in cursor:
            result += row["c"]
        cursor.close()
        conn.close()
        return result