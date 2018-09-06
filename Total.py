import os
import Log_Parser
import Draw_Graph
import Draw_Throughput
import Draw_Block
import Draw_CWND

if __name__ == '__main__':
    file = os.listdir("Log")
    for name in file:
        try:
            Log_Parser.parse(name)
        except:
            pass
        try:
            Draw_Throughput.draw(name)
        except Exception ,e:
            pass
        try:
            Draw_Block.draw(name)
        except:
            pass
        try:
            Draw_CWND.draw(name)
        except Exception, e:
            print e
            pass

    file = os.listdir("Raw")
    for name in file:
        try:
            Draw_Graph.draw(name)
        except:
            pass