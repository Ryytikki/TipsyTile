import pytipsy
import numpy as np

# Duplicate given file creating a tileFactor x tileFactor x tileFactor grid of the original file
# Current version requires file to be bounded in space at [0,1] in each dimension
# Filename   - file to be tiled
# outputName - name of output file
# tileFactor - number of times in each dimension the file is to be tiled
def tipsytile(filename, outputName, tileFactor):
    
    tileFactor3 = tileFactor * tileFactor * tileFactor
    
    # Load in the base data and populate the arrays
    h,g,d,s = rtipsy(filename)
    newg = {'mass' : np.repeat(g['mass'], tileFactor3) , 'x' : g['x'], 'y' : g['y'], 'z' : g['z'], 'vel' : np.repeat(g['vel'], tileFactor3), 'dens' : np.repeat(g['dens'], tileFactor3), 'tempg' : np.repeat(g['tempg'], tileFactor3),
            'h' : np.repeat(g['h'], tileFactor3), 'zmetal' : np.repeat(g['zmetal'], tileFactor3), 'phi' : np.repeat(g['phi'], tileFactor3)}
    newd = {'mass' : np.repeat(d['mass'], tileFactor3), 'x' : d['x'], 'y' : d['y'], 'z' : d['z'], 'vel' : np.repeat(d['vel'], tileFactor3), 'eps' : np.repeat(d['eps'], tileFactor3), 'phi' : np.repeat(d['phi'], tileFactor3)}
    news = {'mass' : np.repeat(s['mass'], tileFactor3), 'x' : s['x'], 'y' : s['y'], 'z' : s['z'], 'vel' : np.repeat(s['vel'], tileFactor3), 'eps' : np.repeat(s['eps'], tileFactor3), 'phi' : np.repeat(s['phi'], tileFactor3), 'metals' : np.repeat(s['metals'], tileFactor3), tform : np.repeat(s['tform'], tileFactor3)}
    
    # Loop through all 3 dimensions
    for x in range(0, tileFactor):
        for y in range(0, tileFactor):
            for z in range(0, tileFactor):
                if x == 0 && y == 0 && z == 0:
                   continue
                # Gas
                newg['x'].append(g['x'] + x)
                newg['y'].append(g['y'] + y)
                newg['z'].append(g['z'] + z)
                # Dark
                newd['x'].append(d['x'] + x)
                newd['y'].append(d['y'] + y)
                newd['z'].append(d['z'] + z)
                # Star
                news['x'].append(s['x'] + x)
                news['y'].append(s['y'] + y)
                news['z'].append(s['z'] + z)

    # Fix header file
    newh = {'time'  : h['time'],
            'n'     : h['n'] * tileFactor3,
            'ndim'  : h['ndim'],
            'ngas'  : h['ngas'] * tileFactor3,
            'ndark' : h['ndark'] * tileFactor3,
            'nstar' : h['nstar'] * tileFactor3}
             
     wtipsy(outputName, newh, newg, newd, news)
