import networkx as nx
import glob
import matplotlib.pyplot as plt
import os
import pickle
from features import degree, assortivity, betweeness,clique_number, clustering_coefficent, coreness, diameter, distortion, eccentricity, edge_connectivity, expansion, girth, hop_count, vertex_connectivity



def get_egos(directory):
    paths = glob.glob("%s/*.edges" % (directory,))
    egos = [int(x.split("/")[-1].split('.')[0]) for x in paths]
    return egos


def construct_network(ego, directory):
    fname = "%s/%d.edges" % (directory, ego)
    f = open(fname,'r')
    net = nx.DiGraph()
    for line in f:
        nodes = [int(x) for x in line.strip().split(' ')]
        [net.add_edge(ego, node) for node in nodes]
        net.add_edge(*nodes)
    f.close()
    return net
    
def plot_features(network_raw_type, d, feat, ylabel):
    plt.plot(d, feat, 'rs')	# b--, g^
    plt.ylabel(ylabel)
    plt.xlabel('Degree')
    plt.title('Network: ' + network_raw_type)
    plt.savefig('../plots/' + ylabel + '.png')


def save_features(network, features):   
    file_feature = open('../features_vector/' + network + '.dat', 'w')
    for f in range(len(features[0])):
        for i in range(len(features)):
            file_feature.write(str(features[i][f]) + ' ')
        file_feature.write('\n') 
    file_feature.close()


def process_network(path):
    d_vector = []
    asso_vector = []
    bet_vector = []
    clique_vector = []
    clust_vector = []
    core_vector = []
    diam_vector = []
    dist_vector = []
    ecc_vector = []
    edgec_vector = []
    ex_vector = []
    gi_vector = []
    hc_vector = []
    vc_vector = []

    egos = get_egos(path)
    networks = [construct_network(ego, path) for ego in egos]
    for i, single_network in enumerate(networks):
        d = degree.d(single_network)
     	asso = assortivity.asso(single_network)
     	bet = betweeness.bet(single_network)
     	clique = clique_number.clique(single_network)
        clust = clustering_coefficent.clust(single_network)
        core = None#coreness.core(single_network) --> to fix
        diam = None#diameter.diam(single_network)
        dist = None#distortion.dist(single_network) --> to fix
        ecc = None#eccentricity.ecc(single_network) --> to fix
        edgec = edge_connectivity.edgec(single_network) #--> too long
        ex = None#expansion.ex(single_network) --> do it
        gi = None#girth.gi(single_network) --> do it
        hc = None#hop_count.hc(single_network)  --> do it
        vc = vertex_connectivity.vc_strong(single_network)

        d_vector.append(d)
        asso_vector.append(asso)
        bet_vector.append(bet)
        clique_vector.append(clique)
        clust_vector.append(clust)
        core_vector.append(core)
        diam_vector.append(diam)
        dist_vector.append(dist)
        ecc_vector.append(ecc)
        edgec_vector.append(edgec)
        ex_vector.append(ex)
        gi_vector.append(gi)
        hc_vector.append(hc)
        vc_vector.append(vc)

    return d_vector, asso_vector, bet_vector, clique_vector, clust_vector, core_vector, diam_vector, dist_vector, ecc_vector, edgec_vector, ex_vector, gi_vector, hc_vector, vc_vector



def main():
    PLOT = 1
    path_to_data = "../data/raw_data/" 
    network_raw_directories = ["twitter"]	#add other directories or make this smarter

    for network_raw_type in network_raw_directories: 
        d, asso, bet, clique, clust, core, diam, dist, ecc, edgec, ex, gi, hc, vc = process_network(path_to_data+network_raw_type)

        if PLOT: 
    	    plot_features(network_raw_type, d, asso, 'Assortivity', )
    	    plot_features(network_raw_type, d, bet, 'Mean Betweness Centrality')
    	    plot_features(network_raw_type, d, clique, 'Mean Clique Number')
            plot_features(network_raw_type, d, clust, 'Average Clustering Coefficient')
            #plot_features(network_raw_type, d, core, 'Coreness') --> to fix
            #plot_features(network_raw_type, d, diam, 'Diameter') #
            #plot_features(network_raw_type, d, dist, 'Distortion')  --> to fix  
            #plot_features(network_raw_type, d, ecc, 'Eccentricity') --> to fix
            plot_features(network_raw_type, d, edgec, 'Egde Connectivity') 
            #plot_features(network_raw_type, d, ex, 'Expansion') ---> to fix
            #plot_features(network_raw_type, d, gi, 'Girth') --> to fix
            #plot_features(network_raw_type, d, hc, 'Hop Count')  --> to fix
            plot_features(network_raw_type, d, vc, 'Vertex Connectivity')


        save_features(network_raw_type, [d, asso, bet, clique, clust, core, diam, dist, ecc, edgec, ex, gi, hc, vc])





if __name__ == '__main__':
    main()
