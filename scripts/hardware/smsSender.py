import serial, time
import dosql

port = raw_input("Serial port: ")
baudrate = input("Baudrate: ")
ser = serial.Serial(port, baudrate)
time.sleep(2)
db = dosql.doSql()

while(True):
    pending_list = db.execqry("SELECT * FROM PendingList()", False)

    for item in pending_list:
        if(len(item) > 1):
            appt_id = str(item[0])
            number = item[1]
            user_message = item[2]
            name = item[3] + " " + item[4]
            appt_time = str(item[5])
            date = str(item[6])

            message = "SPAM: "
            message += name + " has requested an appointment with you on "
            message += date + " at "
            message += appt_time + ". Message: "
            message += user_message

            ser.write(number + "," + message + "\n")

            time.sleep(6)

            print "Ok: " + number + "," + message + "\n"
            db.execqry("SELECT * FROM smsNotified('Pending'," + "'" +  appt_id + "')", True)

    pending_list = []

    response_list = db.execqry("SELECT * FROM ResponseList()", False)

    for item in response_list:
        if(len(item) > 1):
            appt_id = str(item[0])
            number = item[1]
            name = item[2] + " " + item[3]
            status = item[4]

            message = name + " has " + status.lower() + " your appointment request."

            ser.write(number + "," + message + "\n")

            time.sleep(6)

            print "Ok: " + number + "," + message + "\n"
            db.execqry("SELECT * FROM smsNotified" + "('" + status + "'," + "'" +  appt_id + "')", True)

    response_list = []