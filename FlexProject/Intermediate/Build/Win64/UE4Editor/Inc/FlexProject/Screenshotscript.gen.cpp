// Copyright 1998-2018 Epic Games, Inc. All Rights Reserved.
/*===========================================================================
	Generated code exported from UnrealHeaderTool.
	DO NOT modify this manually! Edit the corresponding .h files instead!
===========================================================================*/

#include "GeneratedCppIncludes.h"
#include "Screenshotscript.h"
#ifdef _MSC_VER
#pragma warning (push)
#pragma warning (disable : 4883)
#endif
PRAGMA_DISABLE_DEPRECATION_WARNINGS
void EmptyLinkFunctionForGeneratedCodeScreenshotscript() {}
// Cross Module References
	FLEXPROJECT_API UClass* Z_Construct_UClass_AScreenshotscript_NoRegister();
	FLEXPROJECT_API UClass* Z_Construct_UClass_AScreenshotscript();
	ENGINE_API UClass* Z_Construct_UClass_AActor();
	UPackage* Z_Construct_UPackage__Script_FlexProject();
// End Cross Module References
	void AScreenshotscript::StaticRegisterNativesAScreenshotscript()
	{
	}
	UClass* Z_Construct_UClass_AScreenshotscript_NoRegister()
	{
		return AScreenshotscript::StaticClass();
	}
	UClass* Z_Construct_UClass_AScreenshotscript()
	{
		static UClass* OuterClass = nullptr;
		if (!OuterClass)
		{
			static UObject* (*const DependentSingletons[])() = {
				(UObject* (*)())Z_Construct_UClass_AActor,
				(UObject* (*)())Z_Construct_UPackage__Script_FlexProject,
			};
#if WITH_METADATA
			static const UE4CodeGen_Private::FMetaDataPairParam Class_MetaDataParams[] = {
				{ "IncludePath", "Screenshotscript.h" },
				{ "ModuleRelativePath", "Screenshotscript.h" },
			};
#endif
			static const FCppClassTypeInfoStatic StaticCppClassTypeInfo = {
				TCppClassTypeTraits<AScreenshotscript>::IsAbstract,
			};
			static const UE4CodeGen_Private::FClassParams ClassParams = {
				&AScreenshotscript::StaticClass,
				DependentSingletons, ARRAY_COUNT(DependentSingletons),
				0x00900080u,
				nullptr, 0,
				nullptr, 0,
				nullptr,
				&StaticCppClassTypeInfo,
				nullptr, 0,
				METADATA_PARAMS(Class_MetaDataParams, ARRAY_COUNT(Class_MetaDataParams))
			};
			UE4CodeGen_Private::ConstructUClass(OuterClass, ClassParams);
		}
		return OuterClass;
	}
	IMPLEMENT_CLASS(AScreenshotscript, 2658217350);
	static FCompiledInDefer Z_CompiledInDefer_UClass_AScreenshotscript(Z_Construct_UClass_AScreenshotscript, &AScreenshotscript::StaticClass, TEXT("/Script/FlexProject"), TEXT("AScreenshotscript"), false, nullptr, nullptr, nullptr);
	DEFINE_VTABLE_PTR_HELPER_CTOR(AScreenshotscript);
PRAGMA_ENABLE_DEPRECATION_WARNINGS
#ifdef _MSC_VER
#pragma warning (pop)
#endif
