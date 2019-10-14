#!/bin/sh

export PASS=pass

usage(){
	echo "usage: runabtest.sh [workdir]" 1>&2;
	exit 1
}
dotest(){
	dirtest=$1
	export PYONBROWSER_EMULATEDIR=$dirtest
	jsexe=`mktemp`
	nametest=$2
	namepy=`echo $dirtest/*.py`
	if ! test -f $namepy; then
		echo bad test $dirtest no py file
		return
	fi
	python3 $workdir/ab_test/run_test.py $namepy > $namepy.out 2>&1
	for i in $dirtest/*.out; do
		mv $i $i.native
	done
	python3 main.py --emulate $dirtest --outfile $jsexe $namepy
	js $jsexe > $namepy.out 2>&1
	for i in $dirtest/*.out; do
		if cmp -s $i $i.native; then
			rm $i $i.native
		else
			echo for `basename $namepy` $i is not $i.native
			false
			return
		fi
	done
	echo $nametest pass
}


case $# in
0)
	workdir=`pwd`'/..'
	;;
1)
	workdir=$1
	shift
	;;
*)
	usage
esac

cd $workdir/integ_tests

for t in *_test; do
	if ! test -d $t; then
		continue
	fi
	dirtest=`mktemp -d`
	cp -a $workdir/integ_tests/$t/* $dirtest
	cd $workdir;
	if ! dotest $dirtest $t; then
		export PASS=fail
	fi
done
echo ALL tests $PASS;
if [ $PASS != pass ]; then
	exit 1
fi
exit 0
