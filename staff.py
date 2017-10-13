from flask_restful import Resource, Api, request
from model import conn

class Staffs(Resource):
    """This contain apis to carry out activity with all staffs"""

    def get(self):
        """Retrive list of all the staff"""

        staffs = conn.execute("SELECT * FROM staff ORDER BY stf_date DESC").fetchall()
        return staffs

    def post(self):
        """Add the new staff"""

        staffInput = request.get_json(force=True)
        stf_first_name=staffInput['stf_first_name']
        stf_last_name = staffInput['stf_last_name']
        stf_ph_no = staffInput['stf_ph_no']
        stf_address = staffInput['stf_address']
        staffInput['stf_id']=conn.execute('''INSERT INTO staff(stf_first_name,stf_last_name,stf_ph_no,stf_address)
            VALUES(?,?,?,?)''', (stf_first_name, stf_last_name,stf_ph_no,stf_address)).lastrowid
        conn.commit()
        return staffInput

class Staff(Resource):
    """It include all the apis carrying out the activity with the single staff"""

    def get(self,id):
        """get the details of the stfktor by the staff id"""

        staff = conn.execute("SELECT * FROM staff WHERE stf_id=?",(id,)).fetchall()
        return staff

    def delete(self, id):
        """Delete the staff by its id"""

        conn.execute("DELETE FROM staff WHERE stf_id=?", (id,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,id):
        """Update the staff by its id"""

        staffInput = request.get_json(force=True)
        stf_first_name=staffInput['stf_first_name']
        stf_last_name = staffInput['stf_last_name']
        stf_ph_no = staffInput['stf_ph_no']
        stf_address = staffInput['stf_address']
        conn.execute(
            "UPDATE staff SET stf_first_name=?,stf_last_name=?,stf_ph_no=?,stf_address=? WHERE stf_id=?",
            (stf_first_name, stf_last_name, stf_ph_no, stf_address, id))
        conn.commit()
        return staffInput