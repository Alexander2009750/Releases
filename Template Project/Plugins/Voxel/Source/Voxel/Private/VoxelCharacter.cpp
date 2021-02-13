// Fill out your copyright notice in the Description page of Project Settings.

#include "VoxelCharacter.h"

// Sets default values
AVoxelCharacter::AVoxelCharacter()
{
 	// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;

}

// Called when the game starts or when spawned
void AVoxelCharacter::BeginPlay()
{
	Super::BeginPlay();
	
}

// Called every frame
void AVoxelCharacter::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

}

// Called to bind functionality to input
void AVoxelCharacter::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)
{
	Super::SetupPlayerInputComponent(PlayerInputComponent);

}

