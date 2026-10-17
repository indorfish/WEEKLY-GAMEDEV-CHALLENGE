extends CharacterBody2D


const SPEED = 300.0


func _physics_process(delta):
	#Input stuff
	if Input.is_action_pressed("up"):
		velocity.y = -SPEED
	if Input.is_action_pressed("down"):
		velocity.y = SPEED
	move_and_slide()
	velocity = Vector2(0,0)
	
	#"Seamless cross border movement, like Asteroids the game.
	if position.y > 104:
		position.y = 104
	if position.y < -104:
		position.y = -104

	pass
