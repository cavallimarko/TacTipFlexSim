// Fill out your copyright notice in the Description page of Project Settings.

#include "Screenshotscript.h"
#include "Engine.h"

// Sets default values
AScreenshotscript::AScreenshotscript()
{
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;

}

// Called when the game starts or when spawned
void AScreenshotscript::BeginPlay()
{
	Super::BeginPlay();
	
}

// Called every frame
void AScreenshotscript::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);
	GEngine->AddOnScreenDebugMessage(-1, 5.0f, FColor::Yellow, TEXT("Requesting screenshot")); // display message on window (to check that you are actually calling the lines below)
	FString fileName("C:/Users/Marko/Desktop/TactipSim/Screenshots");
	//FScreenshotRequest::RequestScreenshot(fileName, false, false);

}

