FRAME_COUNT:=200
ALL_PNG:=$(shell ./plotcomplex.py --enumerate ${FRAME_COUNT})

all: animation.mp4

animation.mp4: ${ALL_PNG}
	@rm -f $@
	ffmpeg -framerate 25 -i img_%05d.png -c:v libx264 -pix_fmt yuv420p $@ 2> /dev/null

THIS_FRAME=$(patsubst img_%.png,%,$@)

${ALL_PNG}: img_%.png:
	./plotcomplex.py ${THIS_FRAME} ${FRAME_COUNT}

.PHONY: clean
clean:
	rm -f img_?????.png animation.mp4
