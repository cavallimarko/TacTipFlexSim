// Copyright 1998-2018 Epic Games, Inc. All Rights Reserved.
/*===========================================================================
	Generated code exported from UnrealHeaderTool.
	DO NOT modify this manually! Edit the corresponding .h files instead!
===========================================================================*/

#include "ObjectMacros.h"
#include "ScriptMacros.h"

PRAGMA_DISABLE_DEPRECATION_WARNINGS
#ifdef FLEXPROJECT_RWTextFile_generated_h
#error "RWTextFile.generated.h already included, missing '#pragma once' in RWTextFile.h"
#endif
#define FLEXPROJECT_RWTextFile_generated_h

#define FlexProject_Source_FlexProject_RWTextFile_h_17_RPC_WRAPPERS \
 \
	DECLARE_FUNCTION(execSaveTxt) \
	{ \
		P_GET_PROPERTY(UStrProperty,Z_Param_SaveTextB); \
		P_GET_PROPERTY(UStrProperty,Z_Param_FileNameB); \
		P_FINISH; \
		P_NATIVE_BEGIN; \
		*(bool*)Z_Param__Result=URWTextFile::SaveTxt(Z_Param_SaveTextB,Z_Param_FileNameB); \
		P_NATIVE_END; \
	} \
 \
	DECLARE_FUNCTION(execLoadTxt) \
	{ \
		P_GET_PROPERTY(UStrProperty,Z_Param_FileNameA); \
		P_GET_PROPERTY_REF(UStrProperty,Z_Param_Out_SaveTextA); \
		P_FINISH; \
		P_NATIVE_BEGIN; \
		*(bool*)Z_Param__Result=URWTextFile::LoadTxt(Z_Param_FileNameA,Z_Param_Out_SaveTextA); \
		P_NATIVE_END; \
	}


#define FlexProject_Source_FlexProject_RWTextFile_h_17_RPC_WRAPPERS_NO_PURE_DECLS \
 \
	DECLARE_FUNCTION(execSaveTxt) \
	{ \
		P_GET_PROPERTY(UStrProperty,Z_Param_SaveTextB); \
		P_GET_PROPERTY(UStrProperty,Z_Param_FileNameB); \
		P_FINISH; \
		P_NATIVE_BEGIN; \
		*(bool*)Z_Param__Result=URWTextFile::SaveTxt(Z_Param_SaveTextB,Z_Param_FileNameB); \
		P_NATIVE_END; \
	} \
 \
	DECLARE_FUNCTION(execLoadTxt) \
	{ \
		P_GET_PROPERTY(UStrProperty,Z_Param_FileNameA); \
		P_GET_PROPERTY_REF(UStrProperty,Z_Param_Out_SaveTextA); \
		P_FINISH; \
		P_NATIVE_BEGIN; \
		*(bool*)Z_Param__Result=URWTextFile::LoadTxt(Z_Param_FileNameA,Z_Param_Out_SaveTextA); \
		P_NATIVE_END; \
	}


#define FlexProject_Source_FlexProject_RWTextFile_h_17_INCLASS_NO_PURE_DECLS \
private: \
	static void StaticRegisterNativesURWTextFile(); \
	friend FLEXPROJECT_API class UClass* Z_Construct_UClass_URWTextFile(); \
public: \
	DECLARE_CLASS(URWTextFile, UBlueprintFunctionLibrary, COMPILED_IN_FLAGS(0), 0, TEXT("/Script/FlexProject"), NO_API) \
	DECLARE_SERIALIZER(URWTextFile) \
	enum {IsIntrinsic=COMPILED_IN_INTRINSIC};


#define FlexProject_Source_FlexProject_RWTextFile_h_17_INCLASS \
private: \
	static void StaticRegisterNativesURWTextFile(); \
	friend FLEXPROJECT_API class UClass* Z_Construct_UClass_URWTextFile(); \
public: \
	DECLARE_CLASS(URWTextFile, UBlueprintFunctionLibrary, COMPILED_IN_FLAGS(0), 0, TEXT("/Script/FlexProject"), NO_API) \
	DECLARE_SERIALIZER(URWTextFile) \
	enum {IsIntrinsic=COMPILED_IN_INTRINSIC};


#define FlexProject_Source_FlexProject_RWTextFile_h_17_STANDARD_CONSTRUCTORS \
	/** Standard constructor, called after all reflected properties have been initialized */ \
	NO_API URWTextFile(const FObjectInitializer& ObjectInitializer = FObjectInitializer::Get()); \
	DEFINE_DEFAULT_OBJECT_INITIALIZER_CONSTRUCTOR_CALL(URWTextFile) \
	DECLARE_VTABLE_PTR_HELPER_CTOR(NO_API, URWTextFile); \
DEFINE_VTABLE_PTR_HELPER_CTOR_CALLER(URWTextFile); \
private: \
	/** Private move- and copy-constructors, should never be used */ \
	NO_API URWTextFile(URWTextFile&&); \
	NO_API URWTextFile(const URWTextFile&); \
public:


#define FlexProject_Source_FlexProject_RWTextFile_h_17_ENHANCED_CONSTRUCTORS \
	/** Standard constructor, called after all reflected properties have been initialized */ \
	NO_API URWTextFile(const FObjectInitializer& ObjectInitializer = FObjectInitializer::Get()) : Super(ObjectInitializer) { }; \
private: \
	/** Private move- and copy-constructors, should never be used */ \
	NO_API URWTextFile(URWTextFile&&); \
	NO_API URWTextFile(const URWTextFile&); \
public: \
	DECLARE_VTABLE_PTR_HELPER_CTOR(NO_API, URWTextFile); \
DEFINE_VTABLE_PTR_HELPER_CTOR_CALLER(URWTextFile); \
	DEFINE_DEFAULT_OBJECT_INITIALIZER_CONSTRUCTOR_CALL(URWTextFile)


#define FlexProject_Source_FlexProject_RWTextFile_h_17_PRIVATE_PROPERTY_OFFSET
#define FlexProject_Source_FlexProject_RWTextFile_h_14_PROLOG
#define FlexProject_Source_FlexProject_RWTextFile_h_17_GENERATED_BODY_LEGACY \
PRAGMA_DISABLE_DEPRECATION_WARNINGS \
public: \
	FlexProject_Source_FlexProject_RWTextFile_h_17_PRIVATE_PROPERTY_OFFSET \
	FlexProject_Source_FlexProject_RWTextFile_h_17_RPC_WRAPPERS \
	FlexProject_Source_FlexProject_RWTextFile_h_17_INCLASS \
	FlexProject_Source_FlexProject_RWTextFile_h_17_STANDARD_CONSTRUCTORS \
public: \
PRAGMA_ENABLE_DEPRECATION_WARNINGS


#define FlexProject_Source_FlexProject_RWTextFile_h_17_GENERATED_BODY \
PRAGMA_DISABLE_DEPRECATION_WARNINGS \
public: \
	FlexProject_Source_FlexProject_RWTextFile_h_17_PRIVATE_PROPERTY_OFFSET \
	FlexProject_Source_FlexProject_RWTextFile_h_17_RPC_WRAPPERS_NO_PURE_DECLS \
	FlexProject_Source_FlexProject_RWTextFile_h_17_INCLASS_NO_PURE_DECLS \
	FlexProject_Source_FlexProject_RWTextFile_h_17_ENHANCED_CONSTRUCTORS \
private: \
PRAGMA_ENABLE_DEPRECATION_WARNINGS


#undef CURRENT_FILE_ID
#define CURRENT_FILE_ID FlexProject_Source_FlexProject_RWTextFile_h


PRAGMA_ENABLE_DEPRECATION_WARNINGS
