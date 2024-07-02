from ControlFlow import gen_cfg, to_graph, get_cfg_fromgraph
import argparse

def slurp(f):
    with open(f, 'r') as f: return f.read()


parser = argparse.ArgumentParser()
parser.add_argument('--pythonfile', help='The python file to be analyzed')
args = parser.parse_args()

if __name__ == '__main__':
    g_dict, first, last=get_cfg_fromgraph(slurp(args.pythonfile).strip()) #g_dict is cfg as dict

    cfg=gen_cfg(slurp(args.pythonfile).strip())
    g=to_graph(cfg, arcs=[], name='path_to_graph') #generate .dot graph for cfg
    g.render(format='png')  #generate image
