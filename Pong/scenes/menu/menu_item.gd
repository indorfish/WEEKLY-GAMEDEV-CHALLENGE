class_name menu_item
extends Sprite2D

var n = 1
# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass

func wobble():
	skew =+ sin(n)/2
	n += 0.1



# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
	
