extends Node

@export var parent_node = Node
# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass

func start():
	if Input.is_action_pressed("up_p1"):
		parent_node.velocity.y = -parent_node.SPEED
	if Input.is_action_pressed("down_p1"):
		parent_node.velocity.y = parent_node.SPEED
