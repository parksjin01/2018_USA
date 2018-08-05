import os
import Log_Parser
import Draw_Graph
import Draw_Throughput
import Draw_Block

if __name__ == '__main__':
    file = os.listdir("Log")
    for name in file:
        Log_Parser.parse(name)
        try:
            Draw_Throughput.draw(name)
        except:
            pass
        try:
            Draw_Block.draw(name)
        except:
            pass

    file = os.listdir("Raw")
    for name in file:
        Draw_Graph.draw(name)