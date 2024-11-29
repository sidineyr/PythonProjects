import bpy

# Limpa a cena atual
bpy.ops.wm.read_factory_settings(use_empty=True)

# Configurações de renderização para 1080p a 30 FPS
bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080
bpy.context.scene.render.fps = 30
bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 90  # Duração de 3 segundos a 30 FPS

# Define o caminho de saída do vídeo
bpy.context.scene.render.filepath = "//vinheta_sidiney_rodrigues.mp4"
bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
bpy.context.scene.render.ffmpeg.format = 'MPEG4'
bpy.context.scene.render.ffmpeg.codec = 'H264'
bpy.context.scene.render.ffmpeg.constant_rate_factor = 'HIGH'
bpy.context.scene.render.ffmpeg.ffmpeg_preset = 'GOOD'

# Adiciona o objeto de texto à cena
bpy.ops.object.text_add(location=(0, 0, 0))
text_obj = bpy.context.object
text_obj.data.body = "Sidiney Rodrigues"
text_obj.data.align_x = 'CENTER'
text_obj.data.align_y = 'CENTER'
text_obj.scale = (1.5, 1.5, 1.5)

# Define a posição inicial do
