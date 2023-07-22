import React, { useEffect, useRef } from "react";
import * as THREE from "three";

export default function EightBall({ getLatestReply }) {
  const mount = useRef(null);

  useEffect(() => {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(600, mount.current.clientWidth / mount.current.clientHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer();

    renderer.setSize(mount.current.clientWidth, mount.current.clientHeight);
    mount.current.appendChild(renderer.domElement);

    const geometry = new THREE.SphereGeometry(4, 32, 32);
    const material = new THREE.MeshBasicMaterial({ color: 0xf08080 });
    const sphere = new THREE.Mesh(geometry, material);

    scene.add(sphere);

    camera.position.z = 5;

    const animate = function () {
      requestAnimationFrame(animate);
      sphere.rotation.x += 0.01;
      sphere.rotation.y += 0.01;
      renderer.render(scene, camera);
    };

    animate();

    return () => {
      // cleaning up the mount element when the component is unmounted.
      while (mount.current.firstChild)
        mount.current.removeChild(mount.current.firstChild);
    }
  }, []);

  return <div ref={mount} className="w-96 h-96" />;
}
