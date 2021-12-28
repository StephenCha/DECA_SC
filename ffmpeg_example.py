import ffmpeg # pip install ffmpeg-python

inputDir = './video/'
outputDir = './video_output/'
input_file_name = 'Conan.mp4'

(ffmpeg
 .input(inputDir + input_file_name)
 .filter('fps', fps=10, round = 'up')
 .output(outputDir + "%s-%%04d.jpg"%(input_file_name[:-4]), **{'qscale:v': 3})
 .run())