class_name paddle
extends CharacterBody2D

@export var fake_ball = Node
@export var input_component = Node
var ball = load("res://scenes/ball/ball.tscn")
const SPEED = 300.0
var points = 0
var is_serving: bool = false
@export var paddle_name = ""
@export var parent = Node


func spawn_ball():
	var ball_inst = ball.instantiate()
	ball_inst.position = Vector2(fake_ball.global_position.x + 10, fake_ball.global_position.y)
	fake_ball.hide()
	if paddle_name == "player_1":
		ball_inst.velocity = Vector2(100,0)
	elif paddle_name == "player_2":
		ball_inst.velocity = Vector2(-100,0)
	get_parent().add_child(ball_inst)
	print_tree_pretty()
	
func _physics_process(delta):
	input_component.start()
	move_and_slide()
	velocity = Vector2(0,0)
	
	if is_serving:
		fake_ball.show()
		if Input.is_action_just_pressed("jolt"):
			spawn_ball()
			parent.change_state(parent.states.rally)

	#"Seamless cross border movement, like Asteroids the game.
	if position.y > 104:
		position.y = 104
	if position.y < -104:
		position.y = -104

	pass
