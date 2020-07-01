#!/usr/bin/env python
# -*- coding: utf-8 -*-

from json import dumps, loads
import json
from ws4py.client.threadedclient import WebSocketClient
from time import sleep

class RosBridgeClient(WebSocketClient):

    def opened(self):
        print ("Connection opened...")

    def advertise_topic(self):
        msg = {'op': 'advertise', 'topic': '/haptic_info1',
            'type': 'haptic_parameter/Data'}
        self.send(dumps(msg))

    def closed(self, code, reason=None):
        print (code, reason)

    def received_message(self, m):
        """
        Just print out the message
        """
        try:
            data = json.loads(m.data)
            data_2 = data['msg']
            data_3 =data_2['states']
            data_4 = data_3[0]
            if (data['topic']=="/tibia_rf_contact"):
                fileout = open(r'C:\Users\PandA Lab\Desktop\Telelocomotion\HapticData\Contact\z0.txt','w')
                if(data_4["contact_normals"][0]["z"] > 0.5):
                    fileout.write("1")
                fileout.close()
            elif (data['topic']=="/tibia_lf_contact"):
                fileout = open(r'C:\Users\PandA Lab\Desktop\Telelocomotion\HapticData\Contact\z1.txt','w')
                if(data_4["contact_normals"][0]["z"] > 0.5):
                    fileout.write("1")
                fileout.close()
        except AttributeError:
            a=1
            if (data['topic']=="/tibia_rf_contact"):
                fileout = open(r'C:\Users\PandA Lab\Desktop\Telelocomotion\HapticData\Contact\z0.txt','w')
                fileout.write("0")
                fileout.close()
            elif (data['topic']=="/tibia_lf_contact"):
                fileout = open(r'C:\Users\PandA Lab\Desktop\Telelocomotion\HapticData\Contact\z1.txt','w')
                fileout.write("0")
                fileout.close()

        except IndexError:
            a=2
            if (data['topic']=="/tibia_rf_contact"):
                fileout = open(r'C:\Users\PandA Lab\Desktop\Telelocomotion\HapticData\Contact\z0.txt','w')
                fileout.write("0")
                fileout.close()
            elif (data['topic']=="/tibia_lf_contact"):
                fileout = open(r'C:\Users\PandA Lab\Desktop\Telelocomotion\HapticData\Contact\z1.txt','w')
                fileout.write("0")
                fileout.close()


    def move(self):
        """
        Move the haptics
        """

        try:
            #Device 1
            #Position
            file = open(r'C:\Users\PandA Lab\Desktop\Telelocomotion\HapticData\Device1\position0.txt', 'r')
            to_split = file.read()
            line = to_split.split(", ")
            x=float(line[0])
            y=float(line[1])
            z=float(line[2])

            #Orientation
            file = open(r'C:\Users\PandA Lab\Desktop\Telelocomotion\HapticData\Device1\rotation0Col0.txt', 'r')
            to_split = file.read()
            line = to_split.split(", ")
            m00=float(line[0])
            m10=float(line[1])
            m20=float(line[2])

            file = open(r'C:\Users\PandA Lab\Desktop\Telelocomotion\HapticData\Device1\rotation0Col1.txt', 'r')
            to_split = file.read()
            line = to_split.split(", ")
            m01=float(line[0])
            m11=float(line[1])
            m21=float(line[2])

            file = open(r'C:\Users\PandA Lab\Desktop\Telelocomotion\HapticData\Device1\rotation0Col2.txt', 'r')
            to_split = file.read()
            line = to_split.split(", ")
            m02=float(line[0])
            m12=float(line[1])
            m22=float(line[2])

            #Button
            file = open(r'C:\Users\PandA Lab\Desktop\Telelocomotion\HapticData\Device1\button0A.txt', 'r')
            to_split = file.read()
            line = to_split.split(", ")
            a=float(line[0])
            b=float(line[1])

            #Device2
            #Position
            file = open(r'C:\Users\PandA Lab\Desktop\Telelocomotion\HapticData\Device2\position1.txt', 'r')
            to_split = file.read()
            line = to_split.split(", ")
            X=float(line[0])
            Y=float(line[1])
            Z=float(line[2])

            #Orientation
            file = open(r'C:\Users\PandA Lab\Desktop\Telelocomotion\HapticData\Device2\rotation1Col0.txt', 'r')
            to_split = file.read()
            line = to_split.split(", ")
            M00=float(line[0])
            M10=float(line[1])
            M20=float(line[2])

            file = open(r'C:\Users\PandA Lab\Desktop\Telelocomotion\HapticData\Device2\rotation1Col1.txt', 'r')
            to_split = file.read()
            line = to_split.split(", ")
            M01=float(line[0])
            M11=float(line[1])
            M21=float(line[2])

            file = open(r'C:\Users\PandA Lab\Desktop\Telelocomotion\HapticData\Device2\rotation1Col2.txt', 'r')
            to_split = file.read()
            line = to_split.split(", ")
            M02=float(line[0])
            M12=float(line[1])
            M22=float(line[2])

            #Button
            file = open(r'C:\Users\PandA Lab\Desktop\Telelocomotion\HapticData\Device2\button1A.txt', 'r')
            to_split = file.read()
            line = to_split.split(", ")
            A=float(line[0])
            B=float(line[1])
            msg = {
                'op': 'publish',
                'topic': '/haptic_info1',
                'msg':
                {
                    'point1':
                    {
                        'x' : x,
                        'y' : y,
                        'z' : z,
                    },
                    'rotation1':
                    {
                        'm00' : m00,
                        'm01' : m01,
                        'm02' : m02,
                        'm10' : m10,
                        'm11' : m11,
                        'm12' : m12,
                        'm20' : m20,
                        'm21' : m21,
                        'm22' : m22,
                    },
                    'button1':
                    {
                        'A' : a,
                        'B' : b,
                    },
                    'point2':
                    {
                        'x' : X,
                        'y' : Y,
                        'z' : Z,
                    },
                    'rotation2':
                    {
                        'm00' : M00,
                        'm01' : M01,
                        'm02' : M02,
                        'm10' : M10,
                        'm11' : M11,
                        'm12' : M12,
                        'm20' : M20,
                        'm21' : M21,
                        'm22' : M22,
                    },
                    'button2':
                    {
                        'A' : A,
                        'B' : B,
                    },
                }
            }
            try:
                self.send(dumps(msg))
            except AttributeError:
                a=1

        except ValueError:
            b=1


    def get_data(self):
        msg = {
            'op' : 'subscribe',
            'topic' : '/tibia_rf_contact',
            'type': 'gazebo_msgs/ContactsState'
        }
        self.send(dumps(msg))

    def get_data_2(self):
        msg = {
            'op' : 'subscribe',
            'topic' : '/tibia_lf_contact',
            'type': 'gazebo_msgs/ContactsState'
        }
        self.send(dumps(msg))


if __name__=="__main__":
    try:
        client = RosBridgeClient('ws://10.252.101.75:9090/')
        client.connect()

        client.advertise_topic()
        #client.get_data()
        #client.get_data_2()
        x_value = 1

        while (True):
            client.move()


    except KeyboardInterrupt:
        client.close()
