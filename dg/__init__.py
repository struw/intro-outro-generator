#!/usr/bin/python3

from renderlib import *

def introFrames(p):
	move=50

	# 3 Sekunde Text Fadein
	frames = 3*fps
	for i in range(0, frames):
		yield (
			('text', 'style',    'opacity', "%.4f" % easeLinear(i, 0, 1, frames)),
			('text', 'attr',     'transform', 'translate(%.4f, 0)' % easeOutQuad(i, -move, move, frames)),
		)

	# 2 Sekunden stehen lassen
	frames = 2*fps
	for i in range(0, frames):
		yield ()

	# 3 Sekunde Text Fadeout
	frames = 3*fps
	for i in range(0, frames):
		yield (
			('text', 'style',    'opacity', "%.4f" % easeLinear(i, 1, -1, frames)),
			('text', 'attr',     'transform', 'translate(%.4f, 0)' % easeInQuad(i, 0, move, frames)),
		)

	# two final frames
	for i in range(0, 2):
		yield (
			('text', 'style',    'opacity', "%.4f" % 0),
			('text', 'attr',     'transform', 'translate(%.4f, 0)' % move),
		)

def outroFrames(p):
	# 5 Sekunden stehen bleiben
	frames = 5*fps
	for i in range(0, frames):
		yield []

def debug():
	render(
		'intro.svg',
		'../intro.ts',
		introFrames,
		parameters={
			'$id': 52,
			'$title': 'Reproducible Builds',
			'$person': 'h01ger'
		}
	)

	render(
		'outro.svg',
		'../outro.ts',
		outroFrames
	)

def tasks(queue, args):
	raise NotImplementedError('call with --debug to render your intro/outro')
