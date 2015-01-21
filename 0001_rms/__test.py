#! /usr/bin/env python
# vim: set fileencoding=utf-8: set encoding=utf-8:

"""
This is the test file for the challenge. Specify the path to your script,
and we will run some test vectors against it.
"""

import sys
import subprocess
import math

def test(script, expected, values):
    proc = subprocess.Popen([sys.executable, script], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    proc.stdin.write(' '.join(str(v) for v in values))
    proc.stdin.close()
    output = proc.stdout.read()
    ret = proc.wait()

    value = output.strip()
    correct = (value == str(expected))

    success = ret == 0

    return (correct and success, correct, success, value)

def sinusoid(amplitude=1.0, phase=0.0, dc=0.0, samples_per_cycle=128, cycles=1.0):
    dtheta = 2.0*math.pi / float(samples_per_cycle)
    for i in xrange(int(float(samples_per_cycle)*cycles)):
        yield float(dc) + float(amplitude)*math.sin(float(i)*dtheta + float(phase))

def pulse_train(amplitude=1.0, duty_cycle=0.5, dc=0.0, samples_per_cycle=100, cycles=1.0):
    total_samples = int(float(samples_per_cycle)*float(cycles))
    switch_point = int(float(samples_per_cycle)*float(duty_cycle))
    samples_per_cycle = int(samples_per_cycle)
    for i in xrange(total_samples):
        if (i % samples_per_cycle) < switch_point:
            yield float(dc) + float(amplitude)
        else:
            yield float(dc)

def rads(degs):
    return float(degs)/180.0 * math.pi
    
SQRT2 = math.sqrt(2.0)

test_vectors = (

    (1.0, [1]),
    (0.0, [0,0,0,0]),
    (2.0, [2,2,2,2,2,2]),
    (SQRT2/2.0, sinusoid()),
    (
        math.sqrt(2.67*2.67 + math.pow(4.5/SQRT2, 2.0)),
        sinusoid(4.5, rads(180), dc=2.67)
    ),
    (
        SQRT2/2.0,
        sinusoid(cycles=0.5)
    ),
    (
        3.5*math.sqrt(0.2),
        pulse_train(amplitude=3.5, duty_cycle=0.2)
    ),
)

def main(args=None):
    if args is None:
        args = sys.argv

    if len(args) != 2:
        raise ValueError('Incorrect number of arguments. Specify the path to the script you want tested.')

    script = args[1]

    fails = 0
    for testnum, (expected, values) in enumerate(test_vectors):
        sys.stdout.write("Running test %3d ... " % (testnum,))
        ok, correct, success, value = test(script, expected, values)
        if ok:
            sys.stdout.write('ok\n')
        else:
            fails += 1
            sys.stdout.write('FAILED! Expected %s, got %s\n' % (expected, value))

    total_runs = len(test_vectors)
    print '-----------'
    if fails == 0:
        print "Success! Passed all %d tests." % (total_runs,)
        return 0
    else:
        print "Failed %d / %d tests (%.0f%%)" % (fails, total_runs, float(fails) / float(total_runs))
        return 1


if __name__ == '__main__':
    try:
        exitcode = main()
    except Exception, e:
        raise
        sys.stderr.write('Error: %s\n' % (e,))
        sys.exit(1)
    else:
        sys.exit(exitcode)

