/* DO NOT EDIT THIS FILE - it is machine generated */
#include <jni.h>
/* Header for class com_cypress_cy3240_Cy3240BridgeController */

#ifndef _Included_com_cypress_cy3240_Cy3240BridgeController
#define _Included_com_cypress_cy3240_Cy3240BridgeController
#ifdef __cplusplus
extern "C"
{
#endif

/*
 * Class:     com_cypress_cy3240_Cy3240BridgeController
 * Method:    create
 * Signature: (IIBBB)I
 */
JNIEXPORT jint JNICALL
Java_com_cypress_cy3240_Cy3240BridgeController_create(
        JNIEnv *jenv,
        jobject jobj,
        jint iface,
        jint timeout,
        jbyte power,
        jbyte bus,
        jbyte clock
        );

/*
 * Class:     com_cypress_cy3240_Cy3240BridgeController
 * Method:    open
 * Signature: (I)I
 */
JNIEXPORT jint JNICALL
Java_com_cypress_cy3240_Cy3240BridgeController_open(
        JNIEnv *jenv,
        jobject jobj,
        jint handle
        );

/*
 * Class:     com_cypress_cy3240_Cy3240BridgeController
 * Method:    close
 * Signature: (I)I
 */
JNIEXPORT jint JNICALL
Java_com_cypress_cy3240_Cy3240BridgeController_close(
        JNIEnv *jenv,
        jobject jobj,
        jint handle
        );

/*
 * Class:     com_cypress_cy3240_Cy3240BridgeController
 * Method:    write
 * Signature: (IB[B)I
 */
JNIEXPORT jint JNICALL
Java_com_cypress_cy3240_Cy3240BridgeController_write(
        JNIEnv *jenv,
        jobject jobj,
        jint handle,
        jbyte address,
        jbyteArray dataout
        );

/*
 * Class:     com_cypress_cy3240_Cy3240BridgeController
 * Method:    read
 * Signature: (IB[B)I
 */
JNIEXPORT jint JNICALL
Java_com_cypress_cy3240_Cy3240BridgeController_read(
        JNIEnv *jenv,
        jobject jobj,
        jint handle,
        jbyte address,
        jbyteArray datain
        );

/*
 * Class:     com_cypress_cy3240_Cy3240BridgeController
 * Method:    restart
 * Signature: (I)I
 */
JNIEXPORT jint JNICALL
Java_com_cypress_cy3240_Cy3240BridgeController_restart(
        JNIEnv *jenv,
        jobject jobj,
        jint handle
        );

/*
 * Class:     com_cypress_cy3240_Cy3240BridgeController
 * Method:    reconfigure
 * Signature: (IBBB)I
 */
JNIEXPORT jint JNICALL
Java_com_cypress_cy3240_Cy3240BridgeController_reconfigure(
        JNIEnv *jenv,
        jobject jobj,
        jint handle,
        jbyte power,
        jbyte bus,
        jbyte clock
        );

/*
 * Class:     com_cypress_cy3240_Cy3240BridgeController
 * Method:    reinitialize
 * Signature: (I)I
 */
JNIEXPORT jint JNICALL
Java_com_cypress_cy3240_Cy3240BridgeController_reinitialize(
        JNIEnv *jenv,
        jobject jobj,
        jint handle
        );

#ifdef __cplusplus
}
#endif
#endif
