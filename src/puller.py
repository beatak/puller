#! /usr/bin/env python

import sh
import os
import os.path
# import argparse

def main ():
    cwd = os.getcwd()
    dirs = os.listdir( cwd )
    cleans = {}
    dirties = {}
    for repo in dirs:
        if repo.startswith('.'):
            continue
        if not os.path.isdir( os.path.join(cwd, repo) ):
            continue
        else:
            _repo = os.path.join(cwd, repo)
            _git = os.path.join(_repo, '.git')
            if os.path.exists(_git) and os.path.isdir(_git):
                git = sh.git.bake(_cwd=_repo)
                _status = git.status()
                try:
                    if _status.index( 'working directory clean' ):
                        try:
                            git.pull()
                            cleans[ repo ] = {'pulled': True}
                        except Exception, e:
                            dirties[ repo ] = {'error': str(e).strip()}
                    else:
                        dirties[ repo ] = {'error': _status.strip()}
                except Exception, e:
                    dirties[ repo ] = {'error': 'not staged file(s)'}

    keys_suc = cleans.keys()
    print( "Successfully git-pulled %d repositories" % len(keys_suc) )
    for s in keys_suc:
        print " * %s" % s
    print ""

    keys_failed = dirties.keys()
    print( "Failed with %d repositories" % len(keys_failed) )
    for f in keys_failed:
        print " * %s" % f
        myerr = dirties[ f ]['error'].split('\n')
        output = ''
        if len(myerr) == 1:
            output = myerr[0]
        else:
            for idx, val in enumerate(myerr):
                if len(val) == 0:
                    continue
                else:
                    if val.strip().startswith( 'STDERR' ):
                        output = myerr[idx+1]
                        break
        if len(output) == 0:
            output = ''.join( myerr )[0:78]
        print "   %s" % output

if __name__ == '__main__':
  main()

