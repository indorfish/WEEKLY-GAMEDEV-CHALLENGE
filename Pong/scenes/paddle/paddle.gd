class_name paddle
extends CharacterBody2D

@export var input_component = Node
const SPEED = 300.0


func _physics_process(delta):
	input_component.start()
	move_and_slide()
	velocity = Vector2(0,0)
	
	#"Seamless cross border movement, like Asteroids the game.
	if position.y > 104:
		position.y = 104
	if position.y < -104:
		position.y = -104

	pass
